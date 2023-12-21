def palindrome_of_length_n(s):
    return {i for i in range(len(s)) if s[i] in s[::-1][:i] and s[i] in s[::-1][i+1:]}
