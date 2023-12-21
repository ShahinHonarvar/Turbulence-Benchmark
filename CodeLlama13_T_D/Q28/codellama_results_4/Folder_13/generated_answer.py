
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(47, 81):
        if s[i] not in ascii_values:
            ascii_values.append(ord(s[i]))
    ascii_values.sort()
    return chr(ascii_values[3])
