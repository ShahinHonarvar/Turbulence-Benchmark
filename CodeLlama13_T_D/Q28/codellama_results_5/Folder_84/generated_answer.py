
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[52:79]]
    sorted_ascii_values = sorted(ascii_values, key=lambda x: x % 8 == 0)
    return chr(sorted_ascii_values[6])
