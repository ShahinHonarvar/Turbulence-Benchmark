def palindromes_between_indices(s):
    return set(
        pal for i in range(len(s) - 5) for pal in (s[i:j] for j in range(i, len(s), 2))
    )
