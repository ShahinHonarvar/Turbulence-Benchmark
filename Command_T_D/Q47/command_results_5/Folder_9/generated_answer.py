import re
def palindromes_of_specific_lengths(s):
    if s[0] == s[300]:
        m = re.findall(r'[a-z]{50,60}(?=\Z)', s, flags=re.I)
    else:
        m = re.findall(r'[a-z]{50,60}(?=\Z)', s[:300], flags=re.I)
    return set(m)
