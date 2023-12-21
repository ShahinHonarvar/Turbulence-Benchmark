import re
def palindromes_of_specific_lengths(test_str):
    return set(re.findall(r'[a-z]+\d{2}+[a-z]+', test_str[16:77]))
