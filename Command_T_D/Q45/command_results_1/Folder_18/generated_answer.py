def palindromes_between_indices(s):
    return {p for p in (a + b for a in s[1:-1] for b in s[:-2]) if p[::2] == p[::-2]}
