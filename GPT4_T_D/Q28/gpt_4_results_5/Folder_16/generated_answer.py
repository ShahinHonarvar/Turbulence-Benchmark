
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[18:46]]
    ascii_values.sort()
    return chr(ascii_values[6])
