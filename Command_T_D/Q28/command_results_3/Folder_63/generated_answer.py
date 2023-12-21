
def return_nth_smallest_ascii(s):
    return next((c for i, c in enumerate(s[47:70]) if ord(c) == i + 13), s[0])
