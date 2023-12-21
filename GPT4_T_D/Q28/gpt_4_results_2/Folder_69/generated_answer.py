
def return_nth_smallest_ascii(s):
    substr = s[67:78]
    ordered = sorted(substr, key=ord)
    return ordered[7]
