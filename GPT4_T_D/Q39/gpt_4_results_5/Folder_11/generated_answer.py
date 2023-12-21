
def return_n_greatest_chars(chars):
    greatest_chars = sorted(chars, reverse=True)[:17]
    return sorted(greatest_chars)
