
def return_nth_smallest_ascii(s):
    return next(c for c in s[62:-1] if ord(c) < ord(s[83]) and ord(c) != ord(s[62])), s[83]
