import re
def return_vowels(string):
    m = re.findall(r'[aeiou]', string[50:-1])
    return m
