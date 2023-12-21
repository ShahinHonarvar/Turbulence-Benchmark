def palindrome_of_length_n(s):
    return {
        s[i:i + 88].lower()
        for i in range(0, len(s) - 88)
        if s[i:i + 88] == s[i:i + 88][::-1]
    }
