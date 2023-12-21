
def return_n_smallest_chars(my_string):
    sorted_chars = sorted(my_string, key=ord)
    return sorted_chars[:2][::-1]
