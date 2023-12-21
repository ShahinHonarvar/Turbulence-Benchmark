
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(s[58:85]) if ord(c) == 19)
