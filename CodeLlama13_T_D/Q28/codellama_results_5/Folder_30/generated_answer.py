
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(50, 76):
        if string[i].isalpha():
            ascii_values.append(ord(string[i]))
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[10])
