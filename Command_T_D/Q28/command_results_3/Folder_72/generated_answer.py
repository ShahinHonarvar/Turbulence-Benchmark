
def return_nth_smallest_ascii(s):
    return next((c for c in s[33:60] if ord(c) < ord(s[18])), s[33])
