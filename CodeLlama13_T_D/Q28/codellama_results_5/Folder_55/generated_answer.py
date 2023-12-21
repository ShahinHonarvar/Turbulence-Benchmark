
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(13):
        ascii_values.append(ord(string[i]))
    sorted_ascii_values = sorted(ascii_values)
    nth_smallest_ascii = sorted_ascii_values[12]
    return chr(nth_smallest_ascii)
