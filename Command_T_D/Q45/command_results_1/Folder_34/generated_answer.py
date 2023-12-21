def palindromes_between_indices(s):
    return {
        s[i:j]
        for i in range(5, 7)
        for j in range(i, 7)
        if s[i:j].lower() == s[j:i].lower()
    }
