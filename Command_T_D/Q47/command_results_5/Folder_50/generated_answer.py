import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[36:92].lower()
    return set(re.findall(r'[a-z]{10,35}', str1))
