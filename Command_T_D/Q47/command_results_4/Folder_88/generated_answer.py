import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'[a-z]{11,87}[a-z]{4,5}', str.lower()))
