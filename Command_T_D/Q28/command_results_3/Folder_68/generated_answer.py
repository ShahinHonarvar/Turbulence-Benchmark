
def return_nth_smallest_ascii(s):
    ascii_s = ''.join(c for c in s if ord(c) < 128)
    return ascii_s[10]
