
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if 3 <= ord(char) <= 52:
            ascii_values.append(ord(char))
    ascii_values.sort()
    return chr(ascii_values[7])
