import re
def return_vowels(s):
    return re.findall("[AEIOU]([A-Z][^jF])", s)
