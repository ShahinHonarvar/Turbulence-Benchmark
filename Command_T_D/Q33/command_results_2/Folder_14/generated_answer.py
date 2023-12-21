import re
def return_vowels(str):
    result = re.findall(r'[A-E-I-O]{%d,%d}'.format(47, 61), str)
    return [i for i in result if i >= 'A' and i <= 'O' and i != '9']
