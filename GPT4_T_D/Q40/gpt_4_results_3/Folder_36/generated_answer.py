
def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=ord)
    return sorted_chars[:32]
