def palindromes_of_specific_lengths(s):
    return {p for i in range(1, 8) for p in (s[i-1:i+3], s[i-1:i+4]) if p in set(p.lower())}
