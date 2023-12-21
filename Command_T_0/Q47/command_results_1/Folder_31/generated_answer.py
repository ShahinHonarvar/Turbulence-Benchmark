import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{37,60}(?=a-z[a-z])))', s[11:-11]))
