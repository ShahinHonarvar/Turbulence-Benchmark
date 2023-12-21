def palindromes_between_indices(s):
    return {p for p in range(4, len(s), 2) if s[p-1:p+2].lower() == s[p-1:p+2].lower()}
