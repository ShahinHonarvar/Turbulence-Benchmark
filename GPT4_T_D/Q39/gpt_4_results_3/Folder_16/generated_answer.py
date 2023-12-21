
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    return sorted_chars[:64]
