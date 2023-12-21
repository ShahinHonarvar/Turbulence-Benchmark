
def return_n_smallest_chars(string):
    chars = sorted(string, key=lambda c: ord(c))[:49]
    return sorted(chars, reverse=True)
