
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[51:60]]
    nth_smallest_ascii = sorted(ascii_values)[4]
    return chr(nth_smallest_ascii)
