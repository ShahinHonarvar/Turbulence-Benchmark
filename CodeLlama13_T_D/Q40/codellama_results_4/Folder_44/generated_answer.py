
def return_n_smallest_chars(s):
    chars = sorted(set(s), key=lambda c: ord(c))[:73]
    return ''.join(chars)
