
def return_nth_smallest_ascii(s):
    return next(c for c in s[30:70] if ord(c) == (ord('a') + 14))
