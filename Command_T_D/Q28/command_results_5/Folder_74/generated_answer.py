
def return_nth_smallest_ascii(s):
    return next(a for a in s[1:-1] if ord(a) in range(ord('a') + 1, ord('z') + 1))
