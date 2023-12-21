
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    greatest_chars = sorted_chars[:64]
    return sorted(greatest_chars)
