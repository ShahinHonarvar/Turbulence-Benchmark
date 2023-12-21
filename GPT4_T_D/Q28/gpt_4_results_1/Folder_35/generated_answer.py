
def return_nth_smallest_ascii(s):
    asc_string = sorted([ord(ch) for ch in s[50:76]])
    return chr(asc_string[6])
