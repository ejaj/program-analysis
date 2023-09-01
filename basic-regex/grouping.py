"""
Grouping: Parentheses () are used to group expressions together.
This allows you to apply quantifiers or other operations to multiple characters.
For example, (ab)+ matches "ab" one or more times.
"""
import re

text = "ababcababab"
pattern = r"(ab)+"
matches = re.findall(pattern, text)

print("Matches:", matches)
