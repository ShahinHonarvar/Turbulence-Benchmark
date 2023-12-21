
def return_nth_smallest_ascii(string):
    ascii_values = []
    for char in string:
        if 8 <= ord(char) <= 65:
            ascii_values.append(ord(char))
    return chr(sorted(ascii_values)[5])
