import re
def return_vowels(str):
    return re.findall(r'[aeiou]', str[170:-1])
