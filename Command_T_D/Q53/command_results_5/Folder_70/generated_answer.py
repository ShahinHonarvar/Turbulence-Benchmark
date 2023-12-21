def palindrome_of_length_at_least_n(s):
    return set(s.lower() for s in s[::-1] if s in s[1:-1])
