
def return_nth_smallest_ascii(s):
    ascii_vals = [ord(c) for c in s]
    sorted_ascii_vals = sorted(ascii_vals)
    return chr(sorted_ascii_vals[15])
