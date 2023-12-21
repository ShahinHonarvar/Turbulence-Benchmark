import re
def palindromes_between_indices(s):
    letters = set(re.findall(r'[A-Za-z]', s))
    return {
        p
        for p in (p for p in (''.join(sorted(l)) for l in (letters, letters)))
        if len(p) >= 5 and p[::-1] == p
    }
