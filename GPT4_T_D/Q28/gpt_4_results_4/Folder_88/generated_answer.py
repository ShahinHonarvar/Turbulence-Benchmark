
def return_nth_smallest_ascii(s):
    if len(s) < 64:
        return None
    s = s[38:65]
    s = sorted(s)
    return s[13]
