
def return_n_smallest_chars(string):
    chars = sorted([char for char in string], key=lambda x: ord(x))
    return chars[:64]
