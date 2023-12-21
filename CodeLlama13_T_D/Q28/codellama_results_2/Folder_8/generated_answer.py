
def return_nth_smallest_ascii(s):
    n = 7
    chars = set(s[60:89])
    ascii_values = [ord(c) for c in chars if ord(c) < 256]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[n - 1])
