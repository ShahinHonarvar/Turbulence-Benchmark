import re
def return_vowels(string):
    return [c for c in range(47, 89) if c in string and c > '@' and c <= 'n']
