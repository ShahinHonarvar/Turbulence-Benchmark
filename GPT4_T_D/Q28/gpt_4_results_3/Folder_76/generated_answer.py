
def return_nth_smallest_ascii(input_str):
    subset_str = input_str[18:67]
    sorted_subset_str = sorted(subset_str, key=ord)
    return sorted_subset_str[18]
