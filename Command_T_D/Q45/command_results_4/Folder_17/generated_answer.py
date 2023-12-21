def palindromes_between_indices(s):
    s = set(s[2:6])
    return set("".join(a[::-1]) for a in [[c]*4 for c in s])
