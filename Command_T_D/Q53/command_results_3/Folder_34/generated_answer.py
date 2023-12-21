def palindrome_of_length_at_least_n(s):
    return {p for p in (p for p in s.lower() if p == p[::-1]) if len(p) >= 68}
