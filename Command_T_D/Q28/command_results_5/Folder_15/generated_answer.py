
def return_nth_smallest_ascii(s):
    return next(c for c in s[0:6] if c.isalpha())
