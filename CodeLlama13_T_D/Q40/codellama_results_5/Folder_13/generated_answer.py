
def return_n_smallest_chars(my_string):
    return sorted([char for char in set(my_string)], key=ord)[:31]
