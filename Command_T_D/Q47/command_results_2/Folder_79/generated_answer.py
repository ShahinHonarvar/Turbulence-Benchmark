def palindromes_of_specific_lengths(s):
    return {p for p in s[1:-1].lower() if p[0] in "abcdefghijklmnopqrstuvwxyz" and len(p) in range(3, 5)}
