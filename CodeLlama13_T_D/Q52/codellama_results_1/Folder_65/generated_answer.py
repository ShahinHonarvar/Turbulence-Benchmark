
def palindrome_of_length_n(s):
    return set([w for w in s.split() if len(w) == 35 and w[::-1].lower() == w.lower()])
