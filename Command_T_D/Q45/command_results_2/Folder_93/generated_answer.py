def palindromes_between_indices(s):
    s = s.lower()
    if not s:
        return set()
    if len(s) > 6:
        return set(s[i:j] for i in range(2, len(s) - 5) for j in range(i + 5, len(s)))
    else:
        return set()
