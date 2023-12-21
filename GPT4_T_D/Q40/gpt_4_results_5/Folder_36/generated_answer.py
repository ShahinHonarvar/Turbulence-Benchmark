
def return_n_smallest_chars(string):
    smallest_chars = sorted(string, key=ord)[:32]
    return smallest_chars
