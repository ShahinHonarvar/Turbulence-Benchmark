
def return_nth_smallest_ascii(chars):
    y = sorted([ord(c) for c in chars[47:81]])
    return chr(y[3])
