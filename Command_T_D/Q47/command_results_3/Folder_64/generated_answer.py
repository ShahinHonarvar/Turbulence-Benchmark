import re
def palindromes_of_specific_lengths(test_str):
    result = set(re.findall(r'[a-z]{4,5}', test_str[0:8]))
    return result
