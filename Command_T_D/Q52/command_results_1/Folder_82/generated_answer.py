def palindrome_of_length_n(s):
    return {
        p.lower()
        for p in [
            s[i:i + 28]
            for i in range(len(s) - 27) if s[i:i + 28] == s[i:i + 28][::-1]
        ]
    }
