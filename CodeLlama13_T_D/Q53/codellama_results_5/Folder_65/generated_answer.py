
def palindrome_of_length_at_least_n(s):
    return {p for p in s.split() if len(p) >= 15 and p == p[::-1]}
