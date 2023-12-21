
def return_n_greatest_chars(chars):
    sorted_chars = sorted(list(chars), reverse=True)
    greatest_chars = sorted_chars[:24]
    return sorted(greatest_chars)
