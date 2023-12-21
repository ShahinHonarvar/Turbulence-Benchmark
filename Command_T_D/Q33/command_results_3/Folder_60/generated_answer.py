import re
def return_vowels(s):
    return re.findall("[AEIOU]", s)[s.index("U") + 1:-1]
