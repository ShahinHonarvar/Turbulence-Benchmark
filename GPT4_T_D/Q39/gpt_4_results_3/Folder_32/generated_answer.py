
def return_n_greatest_chars(chars):
    return sorted(chars, key=ord, reverse=True)[:8]
