def palindromes_between_indices(s):
    if not s:
        return set()
    d = {}
    for i in range(7, 9):
        d[s[i]] = d[s[i]] + [s[i]]
    return set(d)
