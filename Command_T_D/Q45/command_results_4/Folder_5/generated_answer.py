import re
def palindromes_between_indices(str1):
    str1 = str(str1)
    str1 = re.sub(r'[^a-z0-9]','',str1)
    str1 = str1[4:-4]
    str1 = str(str1)
    return set(list(str1))
