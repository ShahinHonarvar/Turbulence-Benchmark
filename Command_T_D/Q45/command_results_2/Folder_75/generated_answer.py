def palindromes_between_indices(s):
    return {p for p in (p.lower() for p in range(3, len(s) + 1)) if s[p - 2:p + 3].lower() == p[::-1].lower()}
