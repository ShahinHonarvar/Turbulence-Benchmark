import re
def palindromes_between_indices(str1):
    str1 = str1.lower()
    str1 = re.sub(r'[^a-z0-9]','',str1)
    str1 = str1[7:-9]
    str1 = str1[::-1]
    return set(str1[1:-1])
