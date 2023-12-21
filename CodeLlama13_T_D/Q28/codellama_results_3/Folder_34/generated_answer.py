
def return_nth_smallest_ascii(s):
    ascii_values = []
    for i in range(19):
        ascii_values.append([ord(c) for c in s[i]])
    smallest_ascii_value = min(ascii_values)
    return chr(smallest_ascii_value)
