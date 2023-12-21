import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'[a-z]{23,39}(?=([a-z]))', s[30:75], flags=re.I)
