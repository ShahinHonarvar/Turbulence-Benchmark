def palindromes_between_indices(s):
    return set(p for p in s[3:8].lower() if p[::-1] == p)
