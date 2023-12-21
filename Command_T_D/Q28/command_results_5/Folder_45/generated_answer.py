
def return_nth_smallest_ascii(s):
    return next(c for i, c in enumerate(sorted(s[0:16]), key=lambda x: ord(x)) if i == 15)
