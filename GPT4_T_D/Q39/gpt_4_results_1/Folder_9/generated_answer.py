
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[-20:]
