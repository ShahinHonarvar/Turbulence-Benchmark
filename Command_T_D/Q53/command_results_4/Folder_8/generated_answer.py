def palindrome_of_length_at_least_n(s):
    return set(p for p in (p for p in s.lower() if p[0] == p[-1]) if len(p) >= 45)
