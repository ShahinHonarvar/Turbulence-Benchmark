import re
def palindromes_of_specific_lengths(s):
    res = set(re.findall(r"<(a){55}(a){70}(a){55}(a){70}(a)>", s[14:90], flags=re.I))
    return res
