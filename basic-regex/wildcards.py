"""
Wildcards: The . symbol matches any character except a newline.
"""
import re

"""
1. Match any two characters followed by "at"
"""
text = "The cat sat on the mat."
pattern = r".at"  # Match any two characters followed by "at"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
2. Matching Any Two Characters Followed by "ing":
"""
text = "Singing, dancing, running, and jumping are all fun activities."
pattern = r"..ing"
matches = re.findall(pattern, text)

print("Matches:", matches)

"""
3. Matching Words with "a" in the Middle:
"""
text = "Banana, apple, grape, and orange are fruits."
pattern = r".a."
matches = re.findall(pattern, text)

print("Matches:", matches)
