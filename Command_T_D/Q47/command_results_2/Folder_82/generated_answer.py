import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[3:300]
    return set(re.findall(r'[a-z]+', str1))
