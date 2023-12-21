def palindromes_between_indices(s):
    s = s.lower()
    x = set(s[0:5])
    if len(x) == 0:
        return set()
    return set(x + s[::-1])
