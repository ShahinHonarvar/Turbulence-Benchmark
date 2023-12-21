def palindromes_between_indices(s):
    return {i[::-1] for i in range(3, len(s) + 1) if set(i) <= set(s[1:-1])}
