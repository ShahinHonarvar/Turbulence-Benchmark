import re
def palindromes_between_indices(s):
    str1 = str(re.findall(r'[A-Z][^A-Z]*[A-Z]', s[3:-3], flags=re.I))
    str2 = str(re.findall(r'[A-Z][^A-Z]*[A-Z]', s[4:-2], flags=re.I))
    str3 = str(re.findall(r'[A-Z][^A-Z]*[A-Z]', s[5:-1], flags=re.I))
    return set(str1 + str2 + str3)
