def palindromes_between_indices(s):
    return set(
        ''.join(c for c in s if c.isalpha())[i:j]
        for i in range(1, len(s) - 5) for j in range(i, len(s) - 5)
    )
