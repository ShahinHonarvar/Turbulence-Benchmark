
def return_nth_smallest_ascii(input_str):
    substring = input_str[67:78]
    ascii_values = [ord(char) for char in substring]
    ascii_values.sort()
    return chr(ascii_values[6])
