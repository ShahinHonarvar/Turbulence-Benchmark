
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[44:69]]
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest = sorted_ascii_values[15]
    return chr(nth_smallest)
