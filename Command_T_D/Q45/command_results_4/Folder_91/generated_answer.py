def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    c = set(s[2:6].lower())
    return set(c + c)
