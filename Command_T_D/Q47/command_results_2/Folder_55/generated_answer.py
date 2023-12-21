import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+' + r'(?=([a-z]+){9})' + r'([a-z]+){9}', s[10:-5]))
