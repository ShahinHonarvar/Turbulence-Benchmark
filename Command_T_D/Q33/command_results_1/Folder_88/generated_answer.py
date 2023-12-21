import re
def return_vowels(s):
    return [m.group() for m in re.finditer(r'<(e|i|o|u)', s, flags=re.I)]
