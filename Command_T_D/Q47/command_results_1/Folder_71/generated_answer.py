import re
def palindromes_of_specific_lengths(test_str):
    result = set(re.findall(r'[a-z]{23,36}', test_str[18:65]))
    return result
