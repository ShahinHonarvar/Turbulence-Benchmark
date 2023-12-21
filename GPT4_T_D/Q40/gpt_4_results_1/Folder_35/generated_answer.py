
def return_n_smallest_chars(chars):
    result = sorted(chars, key=lambda x: ord(x))[:7]
    return result
