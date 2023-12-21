
def return_n_greatest_chars(chars):
    chars_ascii = sorted(chars, reverse=True)
    return chars_ascii[:9]
