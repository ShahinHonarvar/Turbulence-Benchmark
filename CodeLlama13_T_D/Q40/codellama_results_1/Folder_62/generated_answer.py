
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=lambda c: ord(c))
    return chars[:84]
