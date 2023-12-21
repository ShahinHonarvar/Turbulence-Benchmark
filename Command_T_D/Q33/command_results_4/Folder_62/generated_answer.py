import re
def return_vowels(s):
    m = re.findall(r'[aeiou]([A-Z])', s)
    return [c for c in m if c[0] > 'D' and c[1] <= 'v']
