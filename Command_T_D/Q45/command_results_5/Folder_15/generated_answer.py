def palindromes_between_indices(s):
    indices = [i for i in range(1, len(s) - 1)]
    return {p for p in range(3, len(s) - 1) if p in indices and p == s[p - 1][::-1].lower()}
