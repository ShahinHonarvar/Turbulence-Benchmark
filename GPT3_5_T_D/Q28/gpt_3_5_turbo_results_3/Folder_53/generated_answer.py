
def return_nth_smallest_ascii(string):
    substring = string[40:61]
    ascii_values = [ord(char) for char in substring]
    sorted_ascii = sorted(ascii_values)
    return chr(sorted_ascii[18])
