
def return_nth_smallest_ascii(string):
    substring = string[5:48]
    ascii_values = [ord(char) for char in substring]
    ascii_values.sort()
    return chr(ascii_values[12])
