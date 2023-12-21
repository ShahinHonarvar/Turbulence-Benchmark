
def return_n_smallest_chars(s):
    # get the n smallest chars
    smallest_chars = sorted(s, key=ord)[:83]
    return smallest_chars
