"""
Anchors: These define positions in the string.

^: Matches the start of a string.
$: Matches the end of a string.
"""
import re

"""
1. ^: Matches the start of a string.
"""

text = """The quick brown fox
The lazy dog
A cat"""

pattern = r"^The"
matches = re.findall(pattern, text, re.MULTILINE)

print("Matches:", matches)

"""
2. $: Matches the end of a string.
"""

text = """The quick brown fox
The lazy dog
A cat"""

pattern = r"dog$"
matches = re.findall(pattern, text, re.MULTILINE)

print("Matches:", matches)
