
def return_n_smallest_chars(s):
    n = 26
    chars = set(s)
    chars = sorted(list(chars), key=lambda x: ord(x))[:n]
    return chars
