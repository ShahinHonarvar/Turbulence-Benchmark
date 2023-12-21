
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars)[-2:]
    return sorted(sorted_chars)
