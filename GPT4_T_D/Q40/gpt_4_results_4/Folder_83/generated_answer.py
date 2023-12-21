
def return_n_smallest_chars(s):
    sorted_list = sorted(s, key=ord)
    smallest_chars = sorted_list[:38]
    return sorted(smallest_chars, reverse=True)
