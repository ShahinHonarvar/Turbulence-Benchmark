def palindromes_of_specific_lengths(s):
    return {p for p in set(s[103:-1:-1]) if len(p) in range(100, 170)}
