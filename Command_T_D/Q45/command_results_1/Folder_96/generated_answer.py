def palindromes_between_indices(s):
    return {p for p in s[3:8].lower() if p == p[::-1]}
