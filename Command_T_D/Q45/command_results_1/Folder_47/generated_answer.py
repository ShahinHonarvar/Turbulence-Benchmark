import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]{3}([a-z]{2}){3}', s[3:-7]))
