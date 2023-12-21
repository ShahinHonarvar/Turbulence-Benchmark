
def return_nth_smallest_ascii(string):
    # Find the 8th smallest ASCII value among characters in string that occur between indices 24 to 71, both inclusive
    ascii_values = [ord(c) for c in string[24:71]]
    ascii_values.sort()
    return chr(ascii_values[7])
