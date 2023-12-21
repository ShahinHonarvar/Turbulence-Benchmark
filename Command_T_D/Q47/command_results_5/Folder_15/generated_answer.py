def palindromes_of_specific_lengths(s):
    return {p for p in set(s[i:i + 3] for i in range(0, len(s) - 2, 3)) if p in set(p[::-1] for p in s[0:6])}
