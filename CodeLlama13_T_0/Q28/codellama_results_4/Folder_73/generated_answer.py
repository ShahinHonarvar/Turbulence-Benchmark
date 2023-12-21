
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(70):
        if string[i] in ascii_values:
            continue
        else:
            ascii_values.append(ord(string[i]))
    return chr(sorted(ascii_values)[9])
