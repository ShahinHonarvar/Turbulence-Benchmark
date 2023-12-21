
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[25:89]]
    sorted_chars = sorted(set(ascii_values))
    return chr(sorted_chars[10])
