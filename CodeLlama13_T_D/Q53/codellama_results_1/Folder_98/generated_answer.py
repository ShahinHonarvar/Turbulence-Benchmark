
def palindrome_of_length_at_least_n(s):
    return {w for w in s.split() if len(w) >= 6 and w == w[::-1]}
