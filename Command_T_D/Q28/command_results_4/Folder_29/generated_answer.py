
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(s[5:-5]) if ord(c) == s[i])
