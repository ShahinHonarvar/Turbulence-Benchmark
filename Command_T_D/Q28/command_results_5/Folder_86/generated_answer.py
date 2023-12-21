
def return_nth_smallest_ascii(s):
    return next((c for c in s[44:69] if ord(c) < ord(s[14])), s[0])
