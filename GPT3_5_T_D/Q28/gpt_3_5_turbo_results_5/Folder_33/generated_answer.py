
def return_nth_smallest_ascii(string):
    substring = string[22:75]
    ascii_values = sorted(ord(char) for char in substring)
    return chr(ascii_values[11])
