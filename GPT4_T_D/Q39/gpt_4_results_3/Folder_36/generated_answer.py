
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=ord, reverse=True)[:32]
    return sorted(sorted_chars)
