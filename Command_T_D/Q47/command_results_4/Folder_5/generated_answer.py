def palindromes_of_specific_lengths(s):
    return set(
        p
        for i in range(63, 70)
        for p in s[i:].lower()
        if p in s[i:][::-1].lower() and len(p) in (4, 5)
    )
