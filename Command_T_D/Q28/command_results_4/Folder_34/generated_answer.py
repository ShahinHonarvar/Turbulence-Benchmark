
def return_nth_smallest_ascii(str):
    return next(c for i, c in enumerate(str) if ord(c) < ord(str[18]))
