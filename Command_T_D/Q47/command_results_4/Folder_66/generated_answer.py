import re
def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    i = 32
    j = 79
    p = re.compile(r'[a-z]+')
    r = set(p.findall(s[i:j]))
    for p in r:
        if len(p) >= 35 and len(p) <= 41:
            yield p
