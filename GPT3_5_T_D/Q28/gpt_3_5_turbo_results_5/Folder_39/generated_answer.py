
def return_nth_smallest_ascii(chars):
    ascii_values = [ord(char) for char in chars[1:67]]
    ascii_values.sort()
    return chr(ascii_values[7])
