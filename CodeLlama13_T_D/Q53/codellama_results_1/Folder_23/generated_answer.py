
def palindrome_of_length_at_least_n(s):
    return {p for p in s.lower() if len(p) >= 19 and p == p[::-1]}
