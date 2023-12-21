def palindrome_of_length_at_least_n(s):
    return {w for w in s.lower() if len(w) >= 4 and w == w[::-1] and all(c.isalnum() for c in w)}
