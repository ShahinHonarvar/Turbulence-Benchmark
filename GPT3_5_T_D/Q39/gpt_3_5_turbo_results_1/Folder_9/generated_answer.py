
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True, key=ord)
    return sorted_chars[:20]
