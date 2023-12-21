
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=ord)
    smallest_chars = sorted_chars[:28]
    return smallest_chars
