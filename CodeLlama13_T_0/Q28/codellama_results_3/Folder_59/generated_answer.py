
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(0, 12):
        ascii_values.append(ord(string[i]))
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[11])
