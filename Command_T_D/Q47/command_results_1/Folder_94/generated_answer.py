def palindromes_of_specific_lengths(s):
    return {p for p in (s[40:94] + s[40:94][::-1]) if 45 <= len(p) <= 51 and all(c.isalpha() for c in p)}
