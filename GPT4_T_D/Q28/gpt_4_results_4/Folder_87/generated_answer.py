
def return_nth_smallest_ascii(input_string):
    subset = input_string[29:34]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[4]
