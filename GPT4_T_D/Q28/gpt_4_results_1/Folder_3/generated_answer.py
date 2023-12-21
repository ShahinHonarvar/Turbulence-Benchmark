
def return_nth_smallest_ascii(string):
    subset_string = string[25:46]
    sorted_string = sorted(subset_string, key=ord)
    return sorted_string[10]
