
def return_n_smallest_chars(str):
    chars = sorted(str)[:23]
    return sorted(chars, reverse=True)
