
def return_nth_smallest_ascii(s):
    return next(c for i,c in enumerate(s) if ord(c) < ord(s[16]) and i < 17)
