
def return_n_smallest_chars(s):
    ascii_list = sorted([char for char in s], key=ord)
    return ascii_list[:10]
