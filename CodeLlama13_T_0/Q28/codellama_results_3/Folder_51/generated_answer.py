
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(10, 74):
        if string[i] not in ascii_values:
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[8])
