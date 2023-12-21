
def return_n_smallest_chars(string):
    chars = set(string)
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[:52]
