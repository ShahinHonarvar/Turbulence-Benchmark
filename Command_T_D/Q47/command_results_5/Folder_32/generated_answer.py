import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'[A-Z]+[A-Z][^A-Z]*[A-Z]+[A-Z][^A-Z]*[A-Z]+[A-Z]+', s[16:77])
