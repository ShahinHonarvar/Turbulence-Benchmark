
def return_nth_smallest_ascii(input_string):
    ascii_codes = [ord(c) for c in input_string[:46]]
    ascii_codes.sort()
    return chr(ascii_codes[9])
