def palindromes_between_indices(s):
    return {s[i:j] for i in range(len(s)-8) for j in range(i+8, len(s)+1)}
