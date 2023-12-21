
def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s[25:46]]
    ascii_vals.sort()
    return chr(ascii_vals[10]) if len(ascii_vals) > 10 else None
