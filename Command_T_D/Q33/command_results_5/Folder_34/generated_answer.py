import re
def return_vowels(s):
    return re.findall(r'[aeiou]([19-32])[0-7]', s)
