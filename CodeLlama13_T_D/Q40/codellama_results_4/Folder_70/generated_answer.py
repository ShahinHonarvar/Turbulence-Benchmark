
def return_n_smallest_chars(string):
    sorted_list = sorted([char for char in set(string)], key=ord)
    return sorted_list[:2]
