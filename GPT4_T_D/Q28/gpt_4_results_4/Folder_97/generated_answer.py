
def return_nth_smallest_ascii(input_string):
    subset_string = input_string[15:22]
    sorted_chars = sorted(subset_string, key=ord)
    return sorted_chars[5]
