import re
def palindromes_of_specific_lengths(s):
    m = re.finditer(r'(?<=.)(.)\1', s[70:-30], flags=re.I)
    return set(x[0] for x in m if len(x[0]) in range(3, 61))
