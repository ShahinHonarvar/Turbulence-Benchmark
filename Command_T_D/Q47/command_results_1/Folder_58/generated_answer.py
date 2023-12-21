def palindromes_of_specific_lengths(s):
    return set(
        [
            p
            for i in range(
                125, 283 + 1, 1
            )
            for j in range(
                max(
                    min(
                        str(10**9),
                        len(p) + 1,
                    )
                    for p in reversed(s[i:j+1]),
                )
            )
            for p in str(i).lower()
            if p == p[::-1]
        ]
    )
