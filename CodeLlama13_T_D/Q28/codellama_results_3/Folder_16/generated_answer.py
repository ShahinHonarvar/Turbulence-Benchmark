
def return_nth_smallest_ascii(string):
    ascii_values = sorted([ord(c) for c in string[18:46]])
    return chr(ascii_values[7])
