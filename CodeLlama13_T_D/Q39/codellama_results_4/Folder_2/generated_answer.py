
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=ord)
    return chars[-48:]
