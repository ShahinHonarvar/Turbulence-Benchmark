
def return_n_smallest_chars(s):
    sorted_list = sorted(s, key=ord)[:84]
    return sorted_list
