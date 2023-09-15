import shutil
import subprocess
import json
import tempfile
import os
from graphviz import Digraph
from dotenv import load_dotenv

load_dotenv()

jar_file_path = os.getenv('JAR_FILE_LOCATION')

if jar_file_path is None:
    raise Exception("JAR_FILE_LOCATION environment variable is not set. Please set it before running the script.")


def generate_class_details_diagram(cls_name, acc_flags, cls_fields, cls_methods):
    """
    Generate a class details diagram using Graphviz.

    :param cls_name: The name of the class.
    :param acc_flags: The access flags of the class.
    :param cls_fields: A list of dictionaries representing class fields, each with 'name' and 'type' keys.
    :param cls_methods: A list of dictionaries representing class methods, each with 'name', 'access_flags',
                        'params' (a list of parameter dictionaries), and 'returns' keys.
    """
    class_details = Digraph('ClassDetails', format='png', engine='dot')

    # Add the class node with class details
    class_details.node('Class', label=f'Class\nName: {cls_name}\nAccess Flags: {acc_flags}')

    # Add the Fields node and fields as subnodes
    class_details.node('Fields', label='Fields')
    for field in cls_fields:
        class_details.node(f'Field_{field["name"]}', label=f'Name: {field["name"]}\nType: {field["type"]}')
        class_details.edge('Fields', f'Field_{field["name"]}', label='Has')

    # Add the Methods node and methods as subnodes
    class_details.node('Methods', label='Methods')
    for method in cls_methods:
        params_str = ", ".join([f'{param["name"]}: {param["type"]}' for param in method['params']])
        class_details.node(f'Method_{method["name"]}',
                           label=f'Name: {method["name"]}\nAccess Flags: {method["access_flags"]}'
                                 f'\nParameters: {params_str}\nReturns: {method["returns"]}')
        class_details.edge('Methods', f'Method_{method["name"]}', label='Has')

    # Save the DOT code to a file
    dot_file_path = 'class_details.dot'
    class_details.save(dot_file_path)

    # Generate the diagram image (PNG)
    subprocess.run(['dot', '-Tpng', '-o', 'class_details.png', dot_file_path])


# Define the fully qualified name of the class you want to disassemble
class_name = 'dtu.deps.simple.Example'

# Create a temporary directory to store extracted class files
temp_dir = tempfile.mkdtemp()
try:
    # Use the jar command to extract the class file
    jar_extraction_command = ['jar', 'xf', jar_file_path, f'{class_name.replace(".", "/")}.class']
    subprocess.run(jar_extraction_command, cwd=temp_dir, check=True)

    # Define the path to the extracted class file
    extracted_class_path = os.path.join(temp_dir, f'{class_name.replace(".", "/")}.class')

    try:
        # Use jvm2json to disassemble the class file
        disassemble_command = ['jvm2json', '-s', extracted_class_path]
        disassemble_output = subprocess.check_output(disassemble_command, universal_newlines=True)
        try:
            json_data = json.loads(disassemble_output)

            # Extract class information
            class_name = json_data["name"]
            access_flags = json_data["access"]
            super_class = json_data["super"]["name"]
            interfaces = json_data["interfaces"]

            # Extract field information
            fields = []
            for field_data in json_data["fields"]:
                field_name = field_data["name"]
                field_type = field_data["type"]["name"]
                fields.append({"name": field_name, "type": field_type})

            # Extract method information
            methods = []
            for method_data in json_data["methods"]:
                method_name = method_data["name"]
                method_access_flags = method_data["access"]
                method_params = []
                for param_data in method_data["params"]:
                    param_type = param_data["type"]["kind"]
                    param_name = param_data["type"]["type"]["name"]
                    param_info = {"type": param_type, "name": param_name}
                    method_params.append(param_info)

                method_returns = method_data["returns"]["type"]
                methods.append({"name": method_name, "access_flags": method_access_flags, "params": method_params,
                                "returns": method_returns})

            # Generate the class details diagram
            generate_class_details_diagram(class_name, access_flags, fields, methods)

            # Print the extracted information
            print("Class Name:", class_name)
            print("Access Flags:", access_flags)
            print("Super Class:", super_class)
            print("Interfaces:", interfaces)
            print("\nFields:")
            for field in fields:
                print(f"Name: {field['name']}, Type: {field['type']}")
            print("\nMethods:")
            for method in methods:
                print(f"Name: {method['name']}, Access Flags: {method['access_flags']}, "
                      f"Parameters: {method['params']}, Returns: {method['returns']}")

        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)

    except subprocess.CalledProcessError as e:
        print("Error executing the jvm2json command:", e)

except subprocess.CalledProcessError as e:
    print("Error executing the jar extraction command:", e)

finally:
    # Clean up: Remove the temporary extraction directory and its contents
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
