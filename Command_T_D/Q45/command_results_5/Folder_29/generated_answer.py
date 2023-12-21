def palindromes_between_indices(s):
    return {s[i][::-1] for i in range(3, len(s)-2)}
