
def return_nth_smallest_ascii(s):
    return next((c for c in s[37:59] if ord(c) < ord(s[36])), s[36])
