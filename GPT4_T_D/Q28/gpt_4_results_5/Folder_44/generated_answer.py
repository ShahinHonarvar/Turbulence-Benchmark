
def return_nth_smallest_ascii(input_string):
    chars_20_to_30 = input_string[20:31]
    sorted_chars = sorted(chars_20_to_30, key=lambda x: ord(x))
    return sorted_chars[7]
