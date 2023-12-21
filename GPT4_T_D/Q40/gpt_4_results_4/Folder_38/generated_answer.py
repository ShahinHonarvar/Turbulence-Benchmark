
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)[:45]
    return sorted_chars
