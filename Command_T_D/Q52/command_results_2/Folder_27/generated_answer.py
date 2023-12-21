def palindrome_of_length_n(s):
    return {i for i in range(len(s)) if s[i] == s[::-1][i-1] and all(c.isalpha() for c in s[i:i+56])}
