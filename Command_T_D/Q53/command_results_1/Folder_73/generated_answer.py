def palindrome_of_length_at_least_n(s):
    return set(s.lower() for i in range(len(s) - 1, -1, -1) if s[i] == s[i][::-1])
