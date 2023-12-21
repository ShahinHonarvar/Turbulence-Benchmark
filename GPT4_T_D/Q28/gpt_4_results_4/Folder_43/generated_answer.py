
def return_nth_smallest_ascii(input_string):
    string_range = input_string[14:36]
    sorted_chars = sorted(string_range, key=ord)
    return sorted_chars[10]
