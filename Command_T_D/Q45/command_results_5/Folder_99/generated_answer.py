import re
def palindromes_between_indices(s):
    r = re.findall(r'[a-z]+|([a-z]+\d+)+[a-z]+', s[4:-8])
    return {p.lower() for p in r if p[::-1] == p}
