
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(70):
        if i < len(string):
            ascii_values.append(ord(string[i]))
    ascii_values.sort()
    return chr(ascii_values[9])
