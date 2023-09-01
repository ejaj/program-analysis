"""
Escape Sequences: Some characters are reserved for special meanings and need to be
escaped with a backslash \ to match them literally.
For example, \. matches a literal period.
"""
import re

text = "The price is $10.99 for each item."
pattern = r"\$10\.99"
matches = re.findall(pattern, text)

print("Matches:", matches)
