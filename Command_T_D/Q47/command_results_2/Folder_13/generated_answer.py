import re
def palindromes_of_specific_lengths(test_str):
    idx = 13
    idx_end = 95
    return set(re.findall(r'[a-z]{1,2}(?=\d{4})[a-z]{1,2}', test_str[idx:idx_end]))
