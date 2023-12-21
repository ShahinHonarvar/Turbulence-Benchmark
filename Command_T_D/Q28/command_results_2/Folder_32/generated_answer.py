
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(sorted(s[14:66]), key=lambda x: ord(x)))
