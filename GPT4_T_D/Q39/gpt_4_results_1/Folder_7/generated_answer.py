
def return_n_greatest_chars(chars):
    return sorted(sorted(chars, key=ord, reverse=True)[:49])
