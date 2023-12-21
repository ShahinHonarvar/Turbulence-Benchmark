
def return_nth_smallest_ascii(s):
    return next(c for c in s[63:-1] if ord(c) < ord(s[76]))
