
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    greatest_chars = sorted_chars[:24]
    return greatest_chars
