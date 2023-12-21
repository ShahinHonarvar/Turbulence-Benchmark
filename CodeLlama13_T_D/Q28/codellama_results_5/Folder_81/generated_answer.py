
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if ord(c) <= 127]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii_value = sorted_ascii_values[13]
    return chr(nth_smallest_ascii_value)
