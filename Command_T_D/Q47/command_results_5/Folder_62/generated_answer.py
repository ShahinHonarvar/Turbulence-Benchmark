import re
def palindromes_of_specific_lengths(str1):
    return set(re.findall(r'(?i)(?=.*[a-z])[a-z]+(?=.*[a-z])[a-z]+', str1[26:-87]))
