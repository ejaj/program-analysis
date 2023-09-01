"""
Literals: These are characters that match themselves.
For example, the regular expression abc will match the exact sequence "abc" in a string.
"""

import re

"""
1. Matching a Specific Word
"""
pattern = r"abc"
text = "The sequence abc is important."

match = re.search(pattern, text)

if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found.")

"""
2. Matching a Specific Phrase
"""
text = "I love ice cream and ice cream loves me."
pattern = r"ice cream"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
3. Matching a Specific Date Format
"""
text = "Today's date is 2023-08-31."
pattern = r"\d{4}-\d{2}-\d{2}"
match = re.search(pattern, text)

if match:
    print("Date found:", match.group())
else:
    print("Date not found.")

"""
4. Matching an Email Address
"""
text = "Contact us at support@example.com or info@sample.org."
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)

print("Email addresses:", matches)

"""
5. Matching Words with Only Letters:
"""
text = "The quick brown fox jumps over 123 lazy dogs."
pattern = r"\b[a-zA-Z]+\b"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
6. Matching Simple Sentences
"""
text = "Alice is running. Bob is jumping. Carol is dancing."
pattern = r"[A-Z][^.!?]*[.!?]"
sentences = re.findall(pattern, text)

print("Sentences:", sentences)
