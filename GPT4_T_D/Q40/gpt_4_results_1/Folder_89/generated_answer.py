
def return_n_smallest_chars(string):
    smallest_chars = sorted(string, key=ord)[:55]
    return smallest_chars
