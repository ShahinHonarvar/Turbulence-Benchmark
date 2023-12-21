import re
def return_vowels(s):
    m = re.fullmatch(r'(?<=.)([aeiou])[a-x]', s)
    return [m.group(1)] if m else []
