
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[17]
    return chr(nth_smallest_ascii)
