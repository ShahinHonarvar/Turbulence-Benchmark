
def palindrome_of_length_n(s):
    return {w for w in s.lower().split() if len(w) == 318 and w[::-1] == w}
