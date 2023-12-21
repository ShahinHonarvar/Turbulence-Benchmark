import re
def return_vowels(s):
    res = re.findall(r'[aeiou]([0-8][^0-9])', s[202:872])
    return [c for c in res if c[1] > 3]
