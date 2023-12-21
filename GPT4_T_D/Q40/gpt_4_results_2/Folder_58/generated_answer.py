
def return_n_smallest_chars(input_str):
    sorted_chars = sorted([c for c in input_str], key=ord)
    return sorted_chars[:49][::-1]
