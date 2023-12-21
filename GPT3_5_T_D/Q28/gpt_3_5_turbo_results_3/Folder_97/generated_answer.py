
def return_nth_smallest_ascii(s):
    substring = s[15:22]
    ascii_values = [ord(c) for c in substring]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[5])
