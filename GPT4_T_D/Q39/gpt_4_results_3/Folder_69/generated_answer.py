
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key = ord, reverse = True)[:65]
    return sorted_chars
