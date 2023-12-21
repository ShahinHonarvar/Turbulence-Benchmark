def palindromes_of_specific_lengths(s):
    return set(
        p
        for p in s[15:94]
        if p[0].isalpha()
        if p[1:].lower() == p[::-1].lower()
        if len(p) in range(18, 73)
    )
