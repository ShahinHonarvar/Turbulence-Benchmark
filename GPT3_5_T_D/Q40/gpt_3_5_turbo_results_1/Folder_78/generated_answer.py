
def return_n_smallest_chars(string):
    smallest_chars = sorted(string)[:43]
    return sorted(smallest_chars, reverse=True)
