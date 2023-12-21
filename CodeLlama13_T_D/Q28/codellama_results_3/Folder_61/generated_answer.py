
def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s if ord(c) <= 127]
    ascii_values.sort()
    return chr(ascii_values[9])
