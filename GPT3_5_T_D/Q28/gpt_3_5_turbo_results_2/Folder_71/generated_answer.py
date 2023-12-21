
def return_nth_smallest_ascii(chars):
    ascii_values = [ord(char) for char in chars[5:83]]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[15])
