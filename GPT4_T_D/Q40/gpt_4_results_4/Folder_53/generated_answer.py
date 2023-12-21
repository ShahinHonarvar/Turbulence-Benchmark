
def return_n_smallest_chars(s):
    sorted_list = sorted(s, key=ord)
    return sorted_list[:19]
