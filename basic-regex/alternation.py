"""
Alternation: The | symbol allows you to match either the expression on the left or the one on the right.
For example, (cat|dog) matches either "cat" or "dog".
"""
import re

text = "I have a cat and a dog as pets."
pattern = r"(cat|dog)"
matches = re.findall(pattern, text)

print("Matches:", matches)
