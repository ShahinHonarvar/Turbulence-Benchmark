
def return_n_smallest_chars(string):
    smallest_chars = sorted(string, key=ord)[:69]
    return smallest_chars
