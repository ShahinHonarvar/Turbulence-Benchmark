
def return_nth_smallest_ascii(s):
    return next(a for a in s[50:-1] if ord(a) < ord(b) for b in s[51:-1])
