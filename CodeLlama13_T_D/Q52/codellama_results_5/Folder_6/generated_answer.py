
def palindrome_of_length_n(s):
    return set(w for w in s if len(w) == 474 and w[::-1].lower() == w.lower())
