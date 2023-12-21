
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[:23]
