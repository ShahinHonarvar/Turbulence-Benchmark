
def return_n_greatest_chars(chars):
    greatest_chars = sorted(chars, reverse=True)[:7]
    return sorted(greatest_chars)
