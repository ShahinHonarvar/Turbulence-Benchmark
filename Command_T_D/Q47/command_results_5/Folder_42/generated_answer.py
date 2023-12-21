import re
def palindromes_of_specific_lengths(test_str):
    #your code here
    return set(re.findall(r'(?i)(?=.*[a-z]){18}(?=.*[a-z]){43}(?=.*[a-z]){95}(?=.*[a-z]){47}(?=.*[a-z])'.format(test_str[43:-95]), test_str))
