import re
def palindromes_between_indices(str1):
    return set(re.findall(r"((?=.)(.)\1)", str1[0:6:2]) + re.findall(r"((?=.)(.)\1)", str1[1:5:-2])
