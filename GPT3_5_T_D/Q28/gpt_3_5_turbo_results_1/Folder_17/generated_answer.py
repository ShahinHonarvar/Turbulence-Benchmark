
def return_nth_smallest_ascii(string):
    sub_string = string[4:34]
    ascii_values = [ord(char) for char in sub_string]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[3])
