import re

one = "#876376f"
two = "#098765"

match = re.search("^#[0-9a-f]{6}$", one)
match2 = re.search("^#[0-9a-f]{6}$", two)


print(match)
print(match2)
