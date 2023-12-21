
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[15:22]]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[6])
