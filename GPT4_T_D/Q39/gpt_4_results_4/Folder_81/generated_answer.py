
def return_n_greatest_chars(chars):
    greatest_chars = sorted(list(chars), reverse=True)[:64]
    return sorted(greatest_chars)
