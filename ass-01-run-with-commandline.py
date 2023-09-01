import argparse
import os
import re
import pygraphviz as pgv

"""
RUN it: python ass-01-run-with-commandline.py /path/to/root_directory --output output_file.png
"""


def find_file(*, folder, reg_pattern):
    """
    Find files in a directory that match a regular expression pattern.

    Args:
        folder (str): The directory to search for files.
        reg_pattern (Pattern): The regular expression pattern to match against filenames.

    Returns:
        List[str]: A list of file paths that match the pattern.
    """
    matching_paths = []
    if os.path.isdir(folder):
        for path, subdir, files in os.walk(folder):
            for file in files:
                if reg_pattern.match(file):
                    matching_paths.append(os.path.join(path, file))
    else:
        print(f"{folder} is not a directory.")
    return matching_paths


def extract_dependencies(*, f_path, reg_pattern):
    """
    Extract dependencies from a Java source file.

    Args:
        f_path (str): The path to the Java source file.
        reg_pattern (Pattern): The regular expression pattern to extract dependencies.

    Returns:
        List[str]: A list of extracted dependencies.
    """
    if not f_path:
        return "Path not found"
    with open(f_path, 'r') as file:
        content = file.read()
    matches = reg_pattern.findall(content)
    dependencies = []
    for match in matches:
        if match[1] and not match[1].startswith("//"):
            dependency = match[1].strip()
            dependencies.append(dependency)
    return dependencies


def create_dependency_graph(root_dir, java_extensions_pattern, dependencies_pattern):
    """
    Create a directed graph of Java code dependencies.

    Args:
        root_dir (str): The root directory to start searching for Java files.
        java_extensions_pattern (Pattern): The regular expression pattern for Java file extensions.
        dependencies_pattern (Pattern): The regular expression pattern to extract dependencies.

    Returns:
        AGraph: A directed graph representing code dependencies.
    """
    graph = pgv.AGraph(directed=True)

    files = find_file(folder=root_dir, reg_pattern=java_extensions_pattern)

    for file_path in files:
        dependencies = extract_dependencies(f_path=file_path, reg_pattern=dependencies_pattern)

        # Add nodes and edges to the graph
        for dependency in dependencies:
            graph.add_edge(file_path, dependency)

    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Java code dependency graph.")
    parser.add_argument("root_dir", help="The root directory to start searching for Java files.")
    parser.add_argument("--output", "-o", default="dependency_graph.png",
                        help="Output file for the dependency graph (default: dependency_graph.png).")

    args = parser.parse_args()

    root_dir = args.root_dir
    java_extensions_pattern = re.compile(r'.*\.java$', re.IGNORECASE)
    dependencies_pattern = re.compile(r'^(.*?import\s+(.*?);|//\s*(.*?import\s+(.*?);))', re.MULTILINE)

    dependency_graph = create_dependency_graph(root_dir, java_extensions_pattern, dependencies_pattern)

    # Specify the output file format based on the file extension
    output_file_format = os.path.splitext(args.output)[1][1:]

    # Render the graph to the output file
    dependency_graph.draw(args.output, format=output_file_format, prog='dot')

    print(f"Dependency graph saved as {args.output}")
