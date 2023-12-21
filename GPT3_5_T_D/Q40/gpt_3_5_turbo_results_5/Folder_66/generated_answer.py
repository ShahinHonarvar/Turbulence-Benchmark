
def return_n_smallest_chars(string):
    sorted_chars = sorted(string)
    n_smallest_chars = sorted_chars[:33]
    return sorted(n_smallest_chars, reverse=True)
