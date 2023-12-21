import re
def return_vowels(s):
    m = re.match(r'(?<=.)[aeiou]', s[10:83])
    if m:
        return m.group()
    else:
        return []
