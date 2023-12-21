
def return_nth_smallest_ascii(s):
    return next((c for c in s[33:-1] if ord(c) < ord(s[32])), s[85])
