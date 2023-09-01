import re

file_path = 'course-02242-examples/src/dependencies/java/dtu/deps/simple/Example.java'

# Read the content of the Java file
with open(file_path, 'r') as file:
    content = file.read()

# Define a regular expression pattern to match all import statements, including commented ones
pattern = re.compile(r'^(.*?import\s+(.*?);|//\s*(.*?import\s+(.*?);))', re.MULTILINE)

# Find all matches of the pattern in the content
matches = pattern.findall(content)

# Print the matched dependencies
dependencies = []
for match in matches:
    if match[1] and not match[1].startswith("//"):
        # If it's not a comment, print the dependency
        dependency = match[1].strip()
        dependencies.append(dependency)
print(dependencies)
