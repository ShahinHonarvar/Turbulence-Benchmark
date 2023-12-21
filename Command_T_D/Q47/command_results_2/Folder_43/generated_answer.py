def palindromes_of_specific_lengths(s):
    return {p for p in s[41:-1] if p in s[42:-1] and p.lower() in s[42:-1] and len(p) in range(23, 39)}
