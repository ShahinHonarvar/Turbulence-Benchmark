def palindromes_between_indices(s):
    if not s:
        return set()
    if len(s) < 6:
        return set()
    return set(a[::-1] for a in [s[i:j] for i in range(1, len(s)-1) for j in range(i+1, len(s))])
