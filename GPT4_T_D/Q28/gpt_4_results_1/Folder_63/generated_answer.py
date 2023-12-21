
def return_nth_smallest_ascii(input_string):
    substring = input_string[47:71]
    sorted_chars = sorted(list(substring))
    return sorted_chars[13]
