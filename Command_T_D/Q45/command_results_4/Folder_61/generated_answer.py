def palindromes_between_indices(s):
    return {w for i in range(len(s) - 6) for j in range(i, i + 7) for w in (s[i:j + 1] + s[j:j + 1]) if w[::-1] == w}
