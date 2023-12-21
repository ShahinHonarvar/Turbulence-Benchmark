
def return_nth_smallest_ascii(string):
    characters = string[9:60]
    ascii_values = [ord(char) for char in characters]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[5])
