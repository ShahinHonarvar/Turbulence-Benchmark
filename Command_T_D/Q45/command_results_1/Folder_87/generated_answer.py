def palindromes_between_indices(s):
    s = set(s)
    return {s[i] + s[i][::-1] for i in range(3, len(s) - 1, 2)}
