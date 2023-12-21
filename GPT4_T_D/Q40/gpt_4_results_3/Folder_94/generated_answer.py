
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)[:87]
    sorted_descending = sorted_chars[::-1]
    return sorted_descending
