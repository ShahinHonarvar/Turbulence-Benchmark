
def return_nth_smallest_ascii(s):
    return next(a for a in s if ord(a) < ord(s[0]) + 15)
