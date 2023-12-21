
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    return sorted_chars[:72]
