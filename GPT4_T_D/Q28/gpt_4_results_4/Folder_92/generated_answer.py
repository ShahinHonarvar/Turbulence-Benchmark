
def return_nth_smallest_ascii(input_string):
    chars_in_range = sorted(input_string[0:4])
    return sorted(chars_in_range, key=ord)[3]
