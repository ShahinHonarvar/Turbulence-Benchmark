
def return_nth_smallest_ascii(input_string):
    sub_string = input_string[1:47]
    sorted_chars = sorted(sub_string, key=ord)
    return sorted_chars[12]
