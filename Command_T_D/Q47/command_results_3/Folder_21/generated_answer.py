def palindromes_of_specific_lengths(s):
    return {p for p in s[100:295].lower() if p[0] in "qwertyuiop" and len(p) in range(136, 161)}
