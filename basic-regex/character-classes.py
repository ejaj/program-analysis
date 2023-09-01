"""
Character Classes: These are used to match specific sets of characters.
For example:
[a-z]: Matches any lowercase letter.
[A-Z]: Matches any uppercase letter.
[0-9]: Matches any digit.
"""
import re

"""
1. Matching Lowercase Letters:
"""
text = "These are used To Match specific sets of characters."
pattern = r"[a-z]+"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
2. Matching Uppercase Letters:
"""
text = "These are used TO Match specific sets of characters."
pattern = r"[A-Z]+"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
3. Matching Digits in a String:
"""
text = "There are 123 apples and 456 oranges."
pattern = r"[0-9]+"
# pattern = r"\d+" //same
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
4. Matching Words Starting with a Vowel:
"""

text = "An apple, an orange, and an elephant."
pattern = r"\b[aeiouAEIOU]\w*\b"
matches = re.findall(pattern, text, re.IGNORECASE)

print("Matches:", matches)

"""
5. Matching Hexadecimal Color Codes:
"""
text = "Colors: #FF3366, #00AABB, and #9922CC."
pattern = r"#([0-9A-Fa-f]{6})"
matches = re.findall(pattern, text)

print("Matches:", matches)
