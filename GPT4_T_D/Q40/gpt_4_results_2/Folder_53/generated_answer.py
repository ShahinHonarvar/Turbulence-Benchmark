
def return_n_smallest_chars(s):
    smallest_chars = sorted(s, key=ord)[:19]
    return smallest_chars
