def palindromes_between_indices(s):
    return set(
        i + j for i in range(1, 8) for j in range(1, 8) if set(i + j).issubset(set(s[1:-1]))
    )
