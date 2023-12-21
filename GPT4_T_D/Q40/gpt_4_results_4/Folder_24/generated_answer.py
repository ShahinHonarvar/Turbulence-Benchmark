
def return_n_smallest_chars(chars):
    sorted_chars = sorted(chars, key=ord)
    top_32_chars = sorted_chars[:32]
    top_32_chars.reverse()
    return top_32_chars
