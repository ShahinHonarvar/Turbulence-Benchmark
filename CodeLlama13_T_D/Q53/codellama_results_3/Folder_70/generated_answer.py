
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    return {w for w in s.split() if len(w) >= 11 and w == w[::-1]}
