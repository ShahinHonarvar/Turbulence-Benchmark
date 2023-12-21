
def palindrome_of_length_n(s):
    return set(w for w in s.split() if len(w) == 423 and w == w[::-1])
