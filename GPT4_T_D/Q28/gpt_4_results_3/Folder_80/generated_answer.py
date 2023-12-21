
def return_nth_smallest_ascii(str_input):
    subset = str_input[51:90]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[13]
