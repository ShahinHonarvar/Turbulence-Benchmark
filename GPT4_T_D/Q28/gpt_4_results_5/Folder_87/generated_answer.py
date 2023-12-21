
def return_nth_smallest_ascii(input_str):
    sliced_str = input_str[29:34]
    sorted_chars = sorted(sliced_str, key = ord)
    return sorted_chars[4]
