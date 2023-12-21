def palindrome_of_length_n(s):
    return set(a for a in (a[::-1] for a in s.lower() if len(a) == 21))
