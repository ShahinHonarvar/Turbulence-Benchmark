import re
def return_vowels(s):
    v = re.findall(r'[aeiou]', s[50:77])
    return [c for c in v if c>s[-1]]
