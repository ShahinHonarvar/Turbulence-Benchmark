
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(sorted(s)) if i < 12)
