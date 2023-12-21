
def return_nth_smallest_ascii(s):
    return next(c for c in s[34:85+1] if ord(c) < ord(s[20])),
