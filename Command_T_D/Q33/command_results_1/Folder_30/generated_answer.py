import re
def return_vowels(s):
    return re.findall(r'[AEIOU][^M^W]', s)[11:-1]
