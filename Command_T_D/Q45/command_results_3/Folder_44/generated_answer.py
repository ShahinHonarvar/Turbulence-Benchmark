def palindromes_between_indices(s):
    return set(
        "".join(sorted(s[i:j + 1].lower()))
        for i in range(2, 8)
        for j in range(i + 1, min(len(s) - 1, i + 7))
    )
