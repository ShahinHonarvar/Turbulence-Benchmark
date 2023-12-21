import re
def return_vowels(s):
    return re.findall(r'[aeiou][^l]d', s)
