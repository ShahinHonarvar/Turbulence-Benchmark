
def return_nth_smallest_ascii(input_string):
    subset_string = input_string[20:31]
    ascii_sorted = sorted(subset_string, key=ord)
    return ascii_sorted[7]
