
def return_nth_smallest_ascii(s):
    ascii_values = sorted(set(s[37:59]))
    return s[ascii_values.index(min(ascii_values[5:]))]
