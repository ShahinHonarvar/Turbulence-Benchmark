
def palindrome_of_length_at_least_n(string, n):
    return {w for w in string if len(w) >= 25 and w == w[::-1]}
