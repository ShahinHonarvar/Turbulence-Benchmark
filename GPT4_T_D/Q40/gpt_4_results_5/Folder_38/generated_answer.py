
def return_n_smallest_chars(chars):
    chars= sorted(chars, key=ord)
    return chars[:45]
