import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?<=.)([a-z]{10,35})\1', s[36:-92].lower()))
