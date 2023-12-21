
def return_n_smallest_chars(string):
    chars = sorted([char for char in set(string)], key=ord)[:11]
    return chars
