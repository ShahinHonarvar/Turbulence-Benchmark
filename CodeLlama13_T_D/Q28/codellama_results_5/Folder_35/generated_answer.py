
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(50, 76):
        if string[i] in string:
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[6])
