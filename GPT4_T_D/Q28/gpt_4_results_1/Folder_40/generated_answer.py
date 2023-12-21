
def return_nth_smallest_ascii(s):
    chars = sorted(s[:5], key=ord)
    return chars[4]
