import re
def return_vowels(str1):
    return re.findall(r'[aeiou]', str1[46:-1])
