import re
def return_vowels(string):
    return re.findall(r'[A-E][^_o]', string)
