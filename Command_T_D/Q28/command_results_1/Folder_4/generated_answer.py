
def return_nth_smallest_ascii(s):
    return next((c for i, c in enumerate(s[9:22]) if ord(c) < ord(s[4])), s[4])
