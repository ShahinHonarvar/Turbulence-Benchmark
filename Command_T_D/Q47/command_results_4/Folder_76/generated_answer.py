def palindromes_of_specific_lengths(s):
    return set(
        (
            s[i:j + 1]
            for i in range(101, min(len(s) - 1, 292) + 1)
            for j in range(max(0, i + 154 - 1), min(len(s) - 1, 182) + 1)
        )
        if s[i:j + 1].lower() == s[i:j + 1][::-1].lower()
    )
