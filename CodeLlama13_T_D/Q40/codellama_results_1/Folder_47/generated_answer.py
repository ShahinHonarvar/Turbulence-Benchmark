
def return_n_smallest_chars(string):
    sorted_list = sorted(string, key=ord)[:21]
    return sorted_list
