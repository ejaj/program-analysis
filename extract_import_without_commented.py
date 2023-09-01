import re

file_path = 'course-02242-examples/src/dependencies/java/dtu/deps/simple/Example.java'

# Read the content of the Java file
with open(file_path, 'r') as file:
    content = file.read()

# Define a regular expression pattern to match import statements
pattern = re.compile(r'^\s*import\s+(.*?);', re.MULTILINE)

# Find all matches of the pattern in the content
matches = pattern.findall(content)

# Print the matched dependencies
for dependency in matches:
    print(dependency)