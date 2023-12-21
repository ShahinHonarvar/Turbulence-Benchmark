
def return_n_greatest_chars(chars):
    n_greatest_chars = sorted(chars, key=ord, reverse=True)[:23]
    return n_greatest_chars
