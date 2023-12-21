
def return_n_smallest_chars(string):
    chars = sorted(string)[:54]
    return sorted(chars, reverse=True)
