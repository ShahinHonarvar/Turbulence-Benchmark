
def return_nth_smallest_ascii(input_string):
    substring = input_string[28:68]
    ascii_values = [ord(ch) for ch in substring]
    ascii_values.sort()
    return chr(ascii_values[14])
