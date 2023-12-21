
def return_nth_smallest_ascii(s):
    return next((c for c in s[42:59] if ord(c) < 117), s[59])
