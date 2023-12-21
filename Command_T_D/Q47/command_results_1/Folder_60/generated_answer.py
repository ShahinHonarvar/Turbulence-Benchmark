import re
def palindromes_of_specific_lengths(str1):
    str1 = str1[23:82]
    return set(re.findall(r'[a-z]{32,34}', str1.lower()))
