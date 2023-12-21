
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    smallest_chars = sorted_chars[:32]
    return smallest_chars
