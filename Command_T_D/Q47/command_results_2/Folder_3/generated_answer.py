import re
def palindromes_of_specific_lengths(str1):
    return set(re.findall(r'[a-z]{49,51}'.lower(), str1[27:-5]))
