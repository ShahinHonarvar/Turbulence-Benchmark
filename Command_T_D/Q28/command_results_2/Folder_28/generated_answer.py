
def return_nth_smallest_ascii(s):
    return next(c for c in s[25:-1] if ord(c) < ord(s[16]) and c not in s[:25] + s[78:])
