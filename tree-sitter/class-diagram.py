from tree_sitter import Language, Parser
from graphviz import Digraph

FILE = "./languages.so"  # the ./ is important
Language.build_library(FILE, ["../tree-sitter-java"])
JAVA_LANGUAGE = Language(FILE, "java")
parser = Parser()
parser.set_language(JAVA_LANGUAGE)

JAVA_SOURCE_FILE = ("/home/kazi/Works/Dtu/program-analysis/course-02242-examples/src/dependencies/java/"
                    "dtu/deps/simple/Example.java")

with open(JAVA_SOURCE_FILE, "rb") as f:
    tree = parser.parse(f.read())

# Assuming you already have the 'tree' object
root_node = tree.root_node

# Define a dictionary to store relationships
relationships = {}
import_names = []
# Iterate over child nodes of the root node
for child in root_node.children:
    if child.type == "import_declaration":
        for declaration in child.children:
            if declaration.type == "scoped_identifier":
                import_name_node = declaration.child_by_field_name("name").text
                if import_name_node:
                    import_names.append(import_name_node.decode('utf-8'))

    if child.type == "class_declaration":
        # Extract the class name from the 'identifier' field of the 'class_declaration' node
        class_name_node = child.child_by_field_name("name")
        class_name = class_name_node.text.decode('utf-8') if class_name_node else "UnknownClass"

        # Initialize a list to store relationships for this class
        relationships[class_name] = []

        class_body_node = child.child_by_field_name("body")
        if class_body_node:
            for class_member in class_body_node.children:
                if class_member.type == "method_declaration":
                    method_modifiers = set()
                    modifier_keywords = {"public", "private", "protected", "static", "final", "abstract", "volatile",
                                         "transient", "synchronized", "native", "strictfp"}

                    for child_member in class_member.children:
                        if child_member.type == "modifiers":
                            for modifier in child_member.children:
                                if modifier.text.decode('utf-8') in modifier_keywords:
                                    method_modifiers.add(modifier.text.decode('utf-8'))

                    method_type_node = class_member.child_by_field_name("type")
                    method_type = method_type_node.text.decode('utf-8') if method_type_node else "void"

                    method_name_node = class_member.child_by_field_name("name")
                    method_name = method_name_node.text.decode('utf-8') if method_name_node else "UnknownMethod"

                    # Check if there's a method body
                    method_declaration_body = class_member.child_by_field_name("body")
                    if method_declaration_body:
                        # print(method_declaration_body.children)

                        for method_expression in method_declaration_body.children:
                            # print(method_invocation)
                            if method_expression.type == "expression_statement":
                                for method_invocation in method_expression.children:
                                    # print(method_invocation)
                                    if method_invocation.type == "method_invocation":
                                        object_name = method_invocation.child_by_field_name("object").text.decode(
                                            'utf-8')
                                        method_invoked = method_invocation.child_by_field_name("name").text.decode(
                                            'utf-8')

                                        relationships[class_name].append(
                                            (method_name, method_modifiers, object_name, method_invoked))
relationships["import_names"] = import_names

# Print the relationships
for key, value in relationships.items():
    if key == "import_names":
        print(f"Import Names: {value}")
    else:
        class_name = key
        relationship_list = value
        for relationship in relationship_list:
            method_name, method_modifiers, object_name, method_invoked = relationship
            print(
                f"Class: {class_name}, Modifiers: {method_modifiers}, Method: {method_name}, Invokes: {object_name}.{method_invoked}")

# Create a Digraph object with a tree layout to represent the class diagram
dot = Digraph(comment='Class Diagram', format='png', graph_attr={'rankdir': 'TB'})

# Add classes and their methods to the diagram
for class_name, relationship_list in relationships.items():
    if class_name == "import_names":
        continue  # Skip import_names in the class diagram

    # Define class attributes
    class_attributes = []
    for relationship in relationship_list:
        _, method_modifiers, object_name, method_invoked = relationship
        class_attributes.append(f"{method_modifiers} {method_invoked}()")

    # Add the class and its methods to the diagram
    dot.node(class_name, f"{class_name}\\n" + "\\n".join(class_attributes))

# Add import names as packages
for import_name in import_names:
    dot.node(import_name, import_name, shape='box')

# Define relationships between classes and import names
for class_name, relationship_list in relationships.items():
    if class_name == "import_names":
        continue

    for relationship in relationship_list:
        _, _, object_name, _ = relationship
        if object_name in import_names:
            dot.edge(class_name, object_name, dir='none')

# Render the diagram to a file (e.g., class_diagram.png)
dot.render('example_class_diagram', format='png')
