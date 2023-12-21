
def return_n_smallest_chars(chars):
    sorted_list = sorted(chars, key=ord)
    return sorted_list[:6][::-1]
