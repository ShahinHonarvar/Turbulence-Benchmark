
def palindrome_of_length_n(s, n):
    return {w for w in s if len(w) == n and w == w[::-1]}
