
def return_nth_smallest_ascii(s):
    return next((c for c in s if ord(c) >= 0x20 and ord(c) <= 0x7E), " ")
