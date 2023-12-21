
def return_n_greatest_chars(chars):
    greatest_chars = sorted(list(chars), reverse=True)[:26]
    return greatest_chars
