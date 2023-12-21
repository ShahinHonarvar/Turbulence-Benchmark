def palindromes_between_indices(s):
    s = set(s[2:-2])
    if not s:
        return set()
    return set(s.upper())
