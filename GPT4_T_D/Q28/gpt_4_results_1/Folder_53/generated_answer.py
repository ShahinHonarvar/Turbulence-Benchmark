
def return_nth_smallest_ascii(string):
    sub_string = string[40:61]
    ascii_values = [ord(ch) for ch in sub_string]
    ascii_values.sort()
    return chr(ascii_values[18])
