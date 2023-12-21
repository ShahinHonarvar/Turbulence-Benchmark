def palindromes_of_specific_lengths(s):
    return {p for p in set(p for i in range(15, 86) for p in s[i:-i]) if len(p) in (51, 52, 53, 54, 55, 56, 57, 58, 59, 60) and p.lower() in s[15:86].lower() and p[0].isalpha() and p[-1].isalpha()}
