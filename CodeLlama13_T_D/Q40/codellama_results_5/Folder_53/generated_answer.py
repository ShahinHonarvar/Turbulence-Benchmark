
def return_n_smallest_chars(s):
    chars = sorted([char for char in s], key=lambda x: ord(x))
    return chars[:19]
