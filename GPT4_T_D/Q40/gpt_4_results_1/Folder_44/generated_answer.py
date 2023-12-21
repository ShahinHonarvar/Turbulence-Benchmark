
def return_n_smallest_chars(chars):
    chars_list = sorted(list(chars))
    result = [c for c in chars_list if ord(c) <= 73]
    return result
