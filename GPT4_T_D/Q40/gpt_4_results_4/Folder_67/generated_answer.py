
def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=ord)[:66]
    return smallest_chars
