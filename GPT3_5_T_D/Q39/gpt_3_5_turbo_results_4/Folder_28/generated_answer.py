
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True)[:3]
    return sorted(sorted_chars)
