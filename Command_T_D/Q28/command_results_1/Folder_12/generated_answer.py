
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(s[3:-26]) if ord(c) < ord(s[i-3]) and ord(c) < ord(s[i+3:-26]) and ord(c) < ord(s[i+26:]))
