
def return_n_smallest_chars(s):
    chars = sorted([char for char in s], key=ord)[:47]
    return chars
