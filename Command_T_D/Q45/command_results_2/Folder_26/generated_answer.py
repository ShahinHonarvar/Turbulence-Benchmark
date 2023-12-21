def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    idx = s[0:4].lower() + s[2:4].lower()
    idx += idx[::-1].lower()
    return set(x[idx[idx.index(x) - 1]:idx[idx.index(x) + 1] for x in range(3, min(len(idx), 6), 2))
