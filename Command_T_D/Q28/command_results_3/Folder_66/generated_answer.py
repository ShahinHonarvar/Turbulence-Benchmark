
def return_nth_smallest_ascii(s):
    return next(c for c in s[35:52] if ord(c) < ord(s[10]))
