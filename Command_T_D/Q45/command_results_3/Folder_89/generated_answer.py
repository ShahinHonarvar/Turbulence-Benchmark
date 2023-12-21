import re
def palindromes_between_indices(s):
    m = re.findall(r'[a-z]+', s[5:-4])
    return {w.lower() for w in m if len(w) >= 6 and w[::-1] == w}
