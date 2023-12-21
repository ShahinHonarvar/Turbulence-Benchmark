
def return_n_smallest_chars(string):
    sorted_list = sorted(list(set(string)), key=ord)
    return sorted_list[:89]
