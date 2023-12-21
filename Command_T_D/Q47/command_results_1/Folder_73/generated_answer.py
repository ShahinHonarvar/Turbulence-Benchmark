import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[21:62]
    return set(re.findall(r'(?i)(?=([a-z]+\1[a-z]+){2,})[a-z]+\1[a-z]+', str1))
