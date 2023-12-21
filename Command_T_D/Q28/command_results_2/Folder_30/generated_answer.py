
def return_nth_smallest_ascii(s):
    return next(c for i,c in enumerate(s) if c.isalpha() and ord(c) in range(ord(s[50:76])))
