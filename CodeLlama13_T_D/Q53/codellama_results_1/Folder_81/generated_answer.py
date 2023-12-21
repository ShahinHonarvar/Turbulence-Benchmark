
def palindrome_of_length_at_least_n(s):
    return {w for w in s.lower().split() if len(w) >= 33 and w == w[::-1]}
