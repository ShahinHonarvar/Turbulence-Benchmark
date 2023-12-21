import re
def return_vowels(string):
    return re.findall(r'[aeiou]', string)[50:77]
