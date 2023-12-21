import re
def palindromes_between_indices(s):
    m = re.findall(r'[a-z]+', s[0:5])
    if not m:
        return set()
    d = set(m)
    d.update(d.translate(str.lower))
    return d
