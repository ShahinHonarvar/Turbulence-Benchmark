
def return_n_smallest_chars(string):
    chars = sorted(set(string), key=lambda x: ord(x))
    return chars[:17]
