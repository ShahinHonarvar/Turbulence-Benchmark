
def return_n_smallest_chars(string):
    return sorted(list(string), key=ord)[:8]
