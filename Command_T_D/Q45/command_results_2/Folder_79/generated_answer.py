import re
def palindromes_between_indices(s):
    try:
        return set(re.findall(r'[a-z]+', s[1:-1], flags=re.I))
    except:
        return set()
