
def return_nth_smallest_ascii(s):
    return next(c for c in s[46:72] if ord(c) < ord(s[46]) + 15)
