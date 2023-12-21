
def return_n_greatest_chars(chars):
    chars = sorted(chars, reverse=True)[:24]
    chars.sort()
    return chars
