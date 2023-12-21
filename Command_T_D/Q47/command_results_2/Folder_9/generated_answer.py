import re
def palindromes_of_specific_lengths(str):
    return set(re.findall(r'[a-z]{50,60}', str[0:301].lower()))
