
def return_nth_smallest_ascii(string):
    subset = string[34:82]
    ascii_values = [ord(char) for char in subset]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[11])
