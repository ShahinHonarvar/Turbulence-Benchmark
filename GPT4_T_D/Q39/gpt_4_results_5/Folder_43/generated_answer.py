
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    ascii_sorted_chars = sorted(sorted_chars, key=ord, reverse=True)
    return ascii_sorted_chars[:56]
