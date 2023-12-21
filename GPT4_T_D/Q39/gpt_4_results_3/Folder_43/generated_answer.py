
def return_n_greatest_chars(chars):
    greatest_chars = sorted(list(chars), key=ord, reverse=True)[:56]
    return greatest_chars
