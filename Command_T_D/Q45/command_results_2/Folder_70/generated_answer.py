import re
def palindromes_between_indices(s):
    m = re.findall(r'[a-z]+', s[1:-1])
    if len(m) >= 4:
        return set(m[0:2] + m[2:-1] + m[-1:])
    else:
        return set()
