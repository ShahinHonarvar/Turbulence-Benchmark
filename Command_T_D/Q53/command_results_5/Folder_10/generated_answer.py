def palindrome_of_length_at_least_n(s):
    return set(s.lower() for i in range(1, 93) if i * 2 <= len(s) and s[i - 1] == s[i * 2 - 1])
