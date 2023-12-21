import re
def palindromes_of_specific_lengths(str1):
    return set(re.findall(r'[a-z]{16,39}([a-z]{16,39})', str1[16:60]))
