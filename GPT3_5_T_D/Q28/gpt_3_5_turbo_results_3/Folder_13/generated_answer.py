
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(47, 81):
        if string[i] in string[:i]:
            continue
        ascii_values.append(ord(string[i]))
        ascii_values.sort()
    return chr(ascii_values[3])
