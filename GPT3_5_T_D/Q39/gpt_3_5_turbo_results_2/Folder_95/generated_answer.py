
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=lambda x: -ord(x))
    return sorted_chars[:36]
