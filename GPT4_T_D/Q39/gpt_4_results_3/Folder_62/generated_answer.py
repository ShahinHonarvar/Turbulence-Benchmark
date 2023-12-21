
def return_n_greatest_chars(chars):
    greatest_chars = sorted(chars, key=ord, reverse=True)[:84]
    return greatest_chars
