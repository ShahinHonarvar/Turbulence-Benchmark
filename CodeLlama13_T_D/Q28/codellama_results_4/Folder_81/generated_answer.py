
def return_nth_smallest_ascii(string):
    ascii_values = []
    for i in range(len(string)):
        if string[i] != " " and string[i] not in ascii_values:
            ascii_values.append(ord(string[i]))
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[13])
