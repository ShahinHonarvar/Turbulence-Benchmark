
def return_nth_smallest_ascii(s):
    return next(c for c in s[29:-47] if ord(c) < ord(s[7])),
