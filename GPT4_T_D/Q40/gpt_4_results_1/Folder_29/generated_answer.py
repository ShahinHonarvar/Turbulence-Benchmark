
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key = ord)[:23]
    return sorted_chars[::-1]
