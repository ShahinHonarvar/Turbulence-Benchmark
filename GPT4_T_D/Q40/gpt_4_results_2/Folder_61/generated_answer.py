
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    smallest_chars = sorted_chars[:66]
    return sorted(smallest_chars, reverse=True)
