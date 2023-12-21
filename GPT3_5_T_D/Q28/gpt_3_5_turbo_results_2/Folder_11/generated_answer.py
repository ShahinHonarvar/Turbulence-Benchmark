
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[9:60]]
    smallest_ascii = sorted(ascii_values)[5]
    return chr(smallest_ascii)
