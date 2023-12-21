
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if char[0] == 'a':
            ascii_values.append(ord('a') - 1)
    for char in string:
        if char[0] == 'b':
            ascii_values.append(ord('b'))
    return chr(min(ascii_values))
