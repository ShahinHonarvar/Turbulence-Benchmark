def palindrome_of_length_n(s):
    return {p for p in s.lower() if p[0] == p[-1] and len(p) == 13}
