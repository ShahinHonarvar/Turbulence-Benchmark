
def return_n_smallest_chars(string):
    ascii_chars = sorted([char for char in string], key=ord)[:75]
    return ascii_chars[::-1]
