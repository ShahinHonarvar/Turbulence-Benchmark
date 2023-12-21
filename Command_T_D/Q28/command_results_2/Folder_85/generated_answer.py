
def return_nth_smallest_ascii(s):
    return next((a for a in s[17:-3] if ord(a) < ord(b) for b in s[17:-3]), None)
