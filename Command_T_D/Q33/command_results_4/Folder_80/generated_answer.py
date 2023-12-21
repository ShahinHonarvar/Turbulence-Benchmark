import re
def return_vowels(s):
    m = re.search(r"((?<=\W)[aeiou])(\W)", s)
    return m.group(1) if m else []
