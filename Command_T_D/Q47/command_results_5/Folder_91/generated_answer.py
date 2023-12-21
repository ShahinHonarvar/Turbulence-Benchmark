def palindromes_of_specific_lengths(s):
    return {
        s[i:i + 3]
        for i in range(len(s) - 3, -1, -1)
        if s[i:i + 3].lower() == s[i:i + 3][::-1].lower()
    }
