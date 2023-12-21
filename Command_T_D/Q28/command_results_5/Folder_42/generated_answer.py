
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(s[12:72]) if ord(c) < ord(s[12]) + 12)
