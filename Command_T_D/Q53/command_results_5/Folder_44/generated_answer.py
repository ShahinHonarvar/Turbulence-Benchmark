def palindrome_of_length_at_least_n(s):
    return set(w for w in s.lower() if len(w)>=89 and w==w[::-1])
