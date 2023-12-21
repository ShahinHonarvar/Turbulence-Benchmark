
def return_nth_smallest_ascii(s):
    return next((c for i, c in enumerate(s) if i < 3 and ord(c) <= ord(s[3])), s[0])
