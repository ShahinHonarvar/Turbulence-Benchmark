import re
def palindromes_between_indices(str1):
    str1 = re.sub(r'[^A-Za-z]+', '', str1)
    str1 = str1[:5] + str1[-5:]
    return set(x.lower() for x in str1 if x[::-1] == x)
