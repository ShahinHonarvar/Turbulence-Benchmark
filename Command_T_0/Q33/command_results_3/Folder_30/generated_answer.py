import re
def return_vowels(s):
    return re.findall(r'[AEIOU][^M]*[A-W]', s)
