import re
def palindromes_of_specific_lengths(s):
    i=26
    j=84
    l=30
    r=46
    return set(re.findall(r'[a-z]{l}(?=([a-z]{r}(?=([a-z]{r}[a-z]{l}))))',s[i:j]))
