
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if ord(c) >= 44 and ord(c) <= 69]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[14])
