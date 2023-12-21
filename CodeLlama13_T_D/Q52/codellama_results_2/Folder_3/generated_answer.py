
def palindrome_of_length_n(s):
    return {w for w in s.split() if len(w) == 100 and w[::-1].lower() == w.lower()}
