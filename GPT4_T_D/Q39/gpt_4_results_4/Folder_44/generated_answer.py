
def return_n_greatest_chars(chars):
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[-73:]
