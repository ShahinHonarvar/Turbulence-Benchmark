
def return_nth_smallest_ascii(input_str):
    valid_chars = input_str[32:68]
    sorted_chars = sorted(valid_chars, key=lambda x: ord(x))
    return sorted_chars[11]
