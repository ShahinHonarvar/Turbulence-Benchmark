
def return_nth_smallest_ascii(string):
    valid_chars = string[48:77]
    sorted_chars = sorted(valid_chars)
    return sorted_chars[4]
