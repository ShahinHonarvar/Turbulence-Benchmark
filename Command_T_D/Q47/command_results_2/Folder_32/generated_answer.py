import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[16:77]
    str1 = re.sub(r'[^A-Za-z]+', '', str1)
    return {x:x for x in str1[::-1].split() if len(x) in range(43, 48)}
