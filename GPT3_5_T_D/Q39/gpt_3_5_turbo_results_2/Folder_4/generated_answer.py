
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, reverse=True, key=lambda x: ord(x))
    return sorted_chars[:90]
