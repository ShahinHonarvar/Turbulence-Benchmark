
def return_nth_smallest_ascii(string):
    substring = string[28:68]
    ascii_values = [ord(char) for char in substring]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[14])
