
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if ord(c) <= 127]
    return chr(sorted(ascii_values)[9])
