
def return_nth_smallest_ascii(string):
    substring = string[51:79]
    ascii_values = [ord(char) for char in substring]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[8])
