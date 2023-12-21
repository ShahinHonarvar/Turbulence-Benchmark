import re
def return_vowels(s):
    return re.findall(r'[aeiou][^m]*[x-z]', s)
