
def return_nth_smallest_ascii(string):
    valid_chars = string[1:32]
    sorted_chars = sorted(valid_chars, key=ord)
    return sorted_chars[5]
