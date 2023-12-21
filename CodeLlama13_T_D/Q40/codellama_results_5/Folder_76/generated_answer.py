
def return_n_smallest_chars(my_string):
    sorted_list = sorted([c for c in set(my_string)], key=ord, reverse=False)[:3]
    return sorted_list
