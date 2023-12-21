
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[58:86]]
    nth_smallest_ascii = sorted(ascii_values)[18]
    return chr(nth_smallest_ascii)
