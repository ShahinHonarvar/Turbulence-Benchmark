
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[10:74]]
    nth_smallest_value = sorted(ascii_values)[8]
    for char, ascii_val in zip(string[10:74], ascii_values):
        if ascii_val == nth_smallest_value:
            return char
