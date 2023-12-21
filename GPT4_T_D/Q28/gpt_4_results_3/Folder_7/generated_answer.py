
def return_nth_smallest_ascii(input_string):
    sliced_string = input_string[12:56]
    sorted_chars = sorted(sliced_string, key=lambda char: ord(char))
    return sorted_chars[16]
