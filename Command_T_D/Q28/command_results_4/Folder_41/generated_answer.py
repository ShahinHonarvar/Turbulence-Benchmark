
def return_nth_smallest_ascii(s):
    return next((c for c in s[58:85] if ord(c) < ord(s[58])), s[58])
