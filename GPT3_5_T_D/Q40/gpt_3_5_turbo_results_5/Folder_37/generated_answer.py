
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars)[:26]
    return sorted_chars[::-1]
