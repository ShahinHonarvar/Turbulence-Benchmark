def palindrome_of_length_at_least_n(s):
    return set(s[i:].lower() for i in range(len(s) - 1) if s[i:i + 2] == s[i:i + 2][::-1])
