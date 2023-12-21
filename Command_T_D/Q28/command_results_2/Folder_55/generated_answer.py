
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(s) if ord(c) < ord(s[12]) and i < 13)
