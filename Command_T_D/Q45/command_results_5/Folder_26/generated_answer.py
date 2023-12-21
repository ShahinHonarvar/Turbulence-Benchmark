import re
def palindromes_between_indices(s):
    s = re.sub(r'[^a-z]+', '', s)
    return {p for p in (''.join(s[4:-6]), ''.join(reversed(s[4:-6]))) if p.lower() == p}
