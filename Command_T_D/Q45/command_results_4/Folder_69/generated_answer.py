def palindromes_between_indices(s):
    return set(a[::-1] for a in (s[i:j] for i in range(len(s) - 3) for j in range(i, len(s) + 1)))
