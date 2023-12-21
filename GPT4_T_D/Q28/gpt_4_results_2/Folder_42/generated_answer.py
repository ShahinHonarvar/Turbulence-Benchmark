
def return_nth_smallest_ascii(input_string):
    subset = input_string[12:73]
    ascii_subset = sorted(subset, key=ord)
    return ascii_subset[12]
