
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[38:65]]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[14])
