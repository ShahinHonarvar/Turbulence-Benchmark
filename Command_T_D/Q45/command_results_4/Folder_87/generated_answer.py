def palindromes_between_indices(s):
    return {
        s[i:i + 9]
        for i in range(len(s) - 8, -1, -1)
        if s[i:i + 9] == s[i][::-1]
    }
