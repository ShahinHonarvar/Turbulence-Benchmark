import re
def return_vowels(s):
    if s[27:57].isalpha():
        return re.findall(r'[aeiou]', s[27:57])
    else:
        return []
