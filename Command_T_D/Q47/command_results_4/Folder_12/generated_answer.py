import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)([a-z]{18})([a-z]{5})([a-z]{5})([a-z]{18})', s[62:-4], flags=re.I))
