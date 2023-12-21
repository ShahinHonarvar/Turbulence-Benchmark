
def return_nth_smallest_ascii(input_string):
    ascii_slice = [ord(c) for c in input_string[22:75]]
    ascii_slice.sort()
    return chr(ascii_slice[11])
