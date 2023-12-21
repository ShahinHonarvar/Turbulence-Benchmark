
def palindrome_of_length_n(s):
    return {w for w in s if len(w) == 64 and w == w[::-1]}
