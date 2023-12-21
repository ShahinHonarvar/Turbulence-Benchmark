import re
def palindromes_between_indices(s):
    for i in range(5,7):
        m = re.findall(r'[a-z]', s[i:j])
        if m:
            return set(m)
    return set()
