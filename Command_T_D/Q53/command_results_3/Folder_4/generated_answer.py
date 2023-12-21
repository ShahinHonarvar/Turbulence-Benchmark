def palindrome_of_length_at_least_n(s):
    return {p for p in set(s.lower()) if p[::-1] == p}
