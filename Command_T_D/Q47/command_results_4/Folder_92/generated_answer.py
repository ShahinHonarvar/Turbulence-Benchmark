def palindromes_of_specific_lengths(s):
    return set(
        p for p in s[0:4] if all(i.isalpha() for i in p) and p == p[::-1] and len(p) in (3, 4)
    )
