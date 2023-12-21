
def return_n_smallest_chars(s):
    chars = sorted(list(set(s)), key=lambda x: ord(x))
    return chars[:65]
