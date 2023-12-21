
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if ord(c) <= 6 and ord(c) >= 0]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_value = sorted_ascii_values[6]
    return chr(nth_smallest_value)
