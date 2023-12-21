
def return_n_smallest_chars(chars):
    sorted_list = sorted(list(chars), key=ord)
    if len(sorted_list) > 76:
        sorted_list = sorted_list[:76]
    return sorted_list
