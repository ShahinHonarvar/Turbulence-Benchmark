
def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=ord)
    return sorted_chars[:26][::-1]
