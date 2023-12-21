import re
def return_vowels(s):
    m = re.search(r"([aeiou])([A-Z])", s)
    if m:
        return [m.group(1)]
    else:
        return []
