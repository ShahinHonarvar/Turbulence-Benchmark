
def return_n_smallest_chars(chars):
    sorted_chars = sorted(list(set(chars)), key = ord)
    return sorted_chars[:33][::-1]
