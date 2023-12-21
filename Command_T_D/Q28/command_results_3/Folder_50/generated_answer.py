
def return_nth_smallest_ascii(s):
    return next(sorted(set(s[25:-4])), s[25])
