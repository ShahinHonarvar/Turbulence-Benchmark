
def return_nth_smallest_ascii(s):
    subs = s[38:83]
    sorted_ascii = sorted([ord(c) for c in subs])
    return chr(sorted_ascii[19])
