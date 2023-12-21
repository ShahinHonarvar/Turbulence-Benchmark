
def return_nth_smallest_ascii(char_string):
    slice_string = char_string[1:37]
    sorted_chars = sorted(slice_string, key=ord)
    return sorted_chars[14]
