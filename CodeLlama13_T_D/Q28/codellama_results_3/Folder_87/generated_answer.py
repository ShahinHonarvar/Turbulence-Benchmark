
def return_nth_smallest_ascii(string):
    ascii_values = {ord(char): char for char in string}
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[29:34]
    return nth_smallest_ascii[4]
