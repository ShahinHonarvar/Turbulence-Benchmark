def palindrome_of_length_n(s):
    return set(s[i:i + 69] for i in range(0, len(s) - 68) if s[i:i + 69] == s[i:i + 69][::-1])
