
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(17, 35):
        char = string[i]
        if char not in ascii_values:
            ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[17])
