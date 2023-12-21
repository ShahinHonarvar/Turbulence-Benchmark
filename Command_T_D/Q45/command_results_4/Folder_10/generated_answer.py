def palindromes_between_indices(s):
    return {
        s[i:j + 1]
        for i in range(len(s) - 1)
        for j in range(i, min(len(s) - 1, i + 6))
    }
