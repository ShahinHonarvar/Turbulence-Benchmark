def palindrome_of_length_n(s):
    return set(s.lower() for i in range(len(s) - 75, -1, -1) if s[i:i + 76] == s[i:i + 76][::-1])
