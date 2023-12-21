
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[1:32]]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[5])
