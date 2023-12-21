
def return_n_smallest_chars(input_str):
    sortable_list = sorted([char for char in input_str], key=ord)
    return sortable_list[:3]
