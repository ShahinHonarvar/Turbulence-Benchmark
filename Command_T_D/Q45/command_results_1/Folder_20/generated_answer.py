def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    s = set(s[2:-2])
    if len(s) < 8:
        return set()
    return set("".join(c for c in s))
