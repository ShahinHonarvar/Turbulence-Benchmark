def palindrome_of_length_n(s):
    return set(s.lower() for i in range(1, len(s) + 1) if s[i - 1] == s[i - 1][::-1])
