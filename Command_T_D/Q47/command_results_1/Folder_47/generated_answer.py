import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]){14}(?i)([a-z]){2})([a-z]){50}(?i)([a-z]){2})([a-z]){14}(?i)[a-z]{%39};%94}' % s, flags=re.I))
