def palindromes_between_indices(s):
    return set(c[0] + s[2:9] + c[1] for c in zip(s[0:2], s[8:]))
