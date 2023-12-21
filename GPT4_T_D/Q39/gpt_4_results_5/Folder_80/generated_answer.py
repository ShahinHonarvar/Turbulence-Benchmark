
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)
    return sorted(sorted_chars[:35])
