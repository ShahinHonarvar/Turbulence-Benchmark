
def return_nth_smallest_ascii(s):
    return next((c for c in s[36:-80] if ord(c) < ord(s[12])), s[12])
