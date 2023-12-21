
def return_n_smallest_chars(my_string):
    sorted_list = sorted([char for char in my_string], key=ord)[:13]
    return list(reversed(sorted_list))
