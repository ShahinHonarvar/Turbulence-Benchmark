
def return_nth_smallest_ascii(text):
    ascii_values = [ord(c) for c in text[12:73]]
    ascii_values.sort()
    return chr(ascii_values[12])
