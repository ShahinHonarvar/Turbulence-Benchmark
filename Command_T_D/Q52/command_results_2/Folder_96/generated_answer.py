def palindrome_of_length_n(s):
    return set(s[i:i + 83] for i in range(0, len(s) - 82) if s[i:i + 83] == s[i:i + 83][::-1])
