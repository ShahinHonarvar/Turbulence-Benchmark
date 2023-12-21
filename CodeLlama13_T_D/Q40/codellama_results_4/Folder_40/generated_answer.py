
def return_n_smallest_chars(string):
    chars = sorted(list(set(string)))
    return [char for char in chars[:7]]
