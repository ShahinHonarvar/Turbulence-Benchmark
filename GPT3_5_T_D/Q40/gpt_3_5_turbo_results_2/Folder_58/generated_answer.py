
def return_n_smallest_chars(characters):
    smallest_chars = sorted(characters)[:49]
    return sorted(smallest_chars, reverse=True)
