import re
def return_vowels(s):
    m = re.match(r'(?<=.)([aeiou])([a-z])', s)
    if m:
        return [m.group(1)]
    return []
