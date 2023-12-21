import re
def return_vowels(s):
    m = re.match(r'[^A-Z0-9]+', s)
    return [c for c in m.group() if c in range(72, 89) and c != 'P']
