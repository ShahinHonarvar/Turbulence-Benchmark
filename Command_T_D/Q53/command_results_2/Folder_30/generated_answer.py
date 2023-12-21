def palindrome_of_length_at_least_n(s):
    return set(s.lower() for s in s.split() if len(s) >= 16 and s[::-1] == s)
