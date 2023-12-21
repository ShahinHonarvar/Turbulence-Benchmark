import re
def palindromes_between_indices(str1):
    str1 = str1[6:-9]
    return set(re.findall(r'[a-z]+', str1.lower()))
