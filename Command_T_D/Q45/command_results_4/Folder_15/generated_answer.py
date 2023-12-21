def palindromes_between_indices(s):
    i = 1
    j = len(s) - 1
    dct = {}
    while i < j:
        c = s[i]
        if c in dct:
            dct[c] += 1
        else:
            dct[c] = 1
        i += 1
    return set(dct.values())
