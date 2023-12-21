
def return_nth_smallest_ascii(characters):
    ascii_values = [ord(char) for char in characters[25:65]]
    ascii_values.sort()
    return chr(ascii_values[5])
