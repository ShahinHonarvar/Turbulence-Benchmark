import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{29,62}(?=([a-z]{11,97})))', s.lower()))
