def palindromes_between_indices(s):
    str_set = set(s)
    return {i * s[i:j] * s[j:i] for i in range(len(s) - 3) for j in range(i + 1, len(s) - 2)}
