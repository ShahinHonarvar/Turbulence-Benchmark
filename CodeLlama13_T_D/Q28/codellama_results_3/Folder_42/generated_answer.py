
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if ord(c) <= 72 and ord(c) >= 12]
    ascii_values.sort()
    return chr(ascii_values[12])
