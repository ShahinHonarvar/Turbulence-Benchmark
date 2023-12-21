def palindrome_of_length_at_least_n(s):
    return {p for p in set(s.lower()) if len(p) >= 53 and p[::-1] == p}
