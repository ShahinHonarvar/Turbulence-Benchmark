import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[31:91]
    str1 = re.findall(r'[a-z]+', str1.lower())
    return set(str1)
