
def palindrome_of_length_at_least_n(s):
    return {p for p in set(s) if len(p) >= 93 and p == p[::-1]}
