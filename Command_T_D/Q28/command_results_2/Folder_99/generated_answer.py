
def return_nth_smallest_ascii(s):
    return next((c for c in s[17:-65:-1] if ord(c) < ord(s[17])), s[17])
