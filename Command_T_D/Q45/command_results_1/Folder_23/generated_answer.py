def palindromes_between_indices(s):
    return set(
        "".join(
            c
            for i in range(len(s) - 1)
            for c in s[i:i + 7]
            if c.lower() in s[i:i + 7]
        )
        for i in range(len(s) - 1)
    )
