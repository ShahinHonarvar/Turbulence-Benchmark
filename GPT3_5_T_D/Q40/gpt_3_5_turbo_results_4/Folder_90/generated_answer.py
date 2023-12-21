
def return_n_smallest_chars(string):
    smallest_chars = sorted(string)[:24]
    return sorted(smallest_chars, reverse=True)
