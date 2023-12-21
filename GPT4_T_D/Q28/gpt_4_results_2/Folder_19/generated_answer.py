
def return_nth_smallest_ascii(string):
    subset_string = string[0:19]
    sorted_subset_string = sorted(subset_string, key=ord)
    return sorted_subset_string[12]
