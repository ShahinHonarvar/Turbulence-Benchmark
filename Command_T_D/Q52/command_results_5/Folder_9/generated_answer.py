def palindrome_of_length_n(s):
    return {i for i in range(len(s) - 72) if s[i:i + 72] == s[i:i + 72][::-1]}
