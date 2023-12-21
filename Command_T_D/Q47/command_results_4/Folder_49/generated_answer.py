import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[10:100]
    pal = set(re.findall(r"([a-z]+[a-z][a-z]+)+", str1, flags=re.I))
    return pal
