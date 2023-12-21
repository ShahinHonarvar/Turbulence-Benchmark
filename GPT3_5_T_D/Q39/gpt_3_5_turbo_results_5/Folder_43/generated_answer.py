
def return_n_greatest_chars(chars):
    return sorted(chars, reverse=True, key=ord)[:56]
