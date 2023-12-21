
def return_nth_smallest_ascii(char_string):
    substr_char = char_string[1:47]
    sorted_char = sorted(substr_char)
    return sorted_char[12]
