
def return_n_smallest_chars(input_str):
    sorted_chars = sorted(input_str, key=ord)
    smallest_chars = sorted_chars[:29]
    return smallest_chars[::-1]
