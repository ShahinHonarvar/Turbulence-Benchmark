
def return_nth_smallest_ascii(s):
    return next((c for c in s[38:-4] if ord(c) < ord(s[62])), s[58])
