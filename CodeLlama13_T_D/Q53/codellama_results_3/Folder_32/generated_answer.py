
def palindrome_of_length_at_least_n(s):
    return set(w for w in s.split() if len(w) >= 70 and w == w[::-1])
