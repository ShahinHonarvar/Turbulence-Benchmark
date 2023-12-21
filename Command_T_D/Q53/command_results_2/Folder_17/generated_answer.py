def palindrome_of_length_at_least_n(s):
    return {p for p in s.lower() if p in s[::-1] and len(p) >= 36}
