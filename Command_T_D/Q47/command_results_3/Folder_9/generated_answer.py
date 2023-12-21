import re
def palindromes_of_specific_lengths(test_str):
    return set(re.findall(r'[A-Z]+\d+[A-Z]+', test_str[0:301], flags=re.I))
