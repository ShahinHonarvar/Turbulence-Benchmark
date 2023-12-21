def palindrome_of_length_at_least_n(s):
    return {p for p in s.lower() if len(p) >= 78 and p[::-1] == p}
