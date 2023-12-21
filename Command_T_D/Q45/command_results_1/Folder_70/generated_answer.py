def palindromes_between_indices(s):
    return {i[::-1] for i in range(len(s) - 3, -1, -1) if all(c.lower() in s[1:6] for c in i)}
