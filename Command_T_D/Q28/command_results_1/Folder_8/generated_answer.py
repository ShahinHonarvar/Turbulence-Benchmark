
def return_nth_smallest_ascii(s):
    return next((c for c in s[60:88+1] if ord(c) < ord(s[60])), s[60])
