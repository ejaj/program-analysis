"""
Quantifiers: These specify how many times a preceding element should appear.
For example:
*: Matches zero or more occurrences.
+: Matches one or more occurrences.
?: Matches zero or one occurrence.
{n}: Matches exactly n occurrences.
{n,}: Matches n or more occurrences.
{n,m}: Matches between n and m occurrences.
"""
import re

"""
1. *: Matches zero or more occurrences
"""
text = "The report was red, but it could be redder."
pattern = r"re*d"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
2. +: Matches one or more occurrences
"""
text = "She said hiiiiii to him."
pattern = r"hi+"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
3. ?: Matches zero or one occurrence
"""

text = "You may have color or colour."
pattern = r"colou?r"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
4. {n}: Matches exactly n occurrences
"""
text = "The number is 12345 and 345444."
pattern = r"\d{3}"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
5. {n,}: Matches n or more occurrences
"""

text = "She said hii to hiim hi."
pattern = r"hi{2,}"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
5. {n,m}: Matches between n and m occurrences
"""

text = "She said hiiiiii to him."
pattern = r"hi{2,4}"
matches = re.findall(pattern, text)

print("Matches:", matches)
