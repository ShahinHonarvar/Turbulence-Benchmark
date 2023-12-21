def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return {p for p in [p for p in s if p[0] == p[-1]] if len(p) >= 66}
