def palindrome_of_length_at_least_n(s):
    return set(p for p in s.lower() if p[0] == p[-1] and len(p) >= 6)
