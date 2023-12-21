
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if 0 <= ord(char) <= 69]
    ascii_values.sort()
    return chr(ascii_values[9])
