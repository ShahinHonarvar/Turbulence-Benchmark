
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    five_smallest_chars = sorted_chars[:5]
    return five_smallest_chars
