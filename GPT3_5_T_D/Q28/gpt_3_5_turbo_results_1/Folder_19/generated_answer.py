
def return_nth_smallest_ascii(string):
    sub_string = string[0:19]
    ascii_values = [ord(char) for char in sub_string]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[12])
