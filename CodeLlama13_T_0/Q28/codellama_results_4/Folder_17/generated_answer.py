
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(4, 34):
        if string[i] not in ascii_values:
            ascii_values.append(ord(string[i]))
    ascii_values.sort()
    return chr(ascii_values[3])
