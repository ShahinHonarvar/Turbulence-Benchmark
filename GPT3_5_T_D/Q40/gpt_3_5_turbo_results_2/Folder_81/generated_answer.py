
def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort()
    return chars[:64]
