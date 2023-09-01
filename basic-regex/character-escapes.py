"""
Character Escapes: Backslashes can be used to escape special characters, so they're treated as literals.
For example, \d matches any digit character.
"""
import re

text = "The product costs $25.99."
pattern = r"\d+"
matches = re.findall(pattern, text)

print("Matches:", matches)
