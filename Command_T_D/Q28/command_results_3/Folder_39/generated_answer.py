
def return_nth_smallest_ascii(s):
    return next((a for a in s[1:-1] if ord(a) < ord(s[0])), s[0])
