
def return_n_greatest_chars(s):
    greatest_chars = sorted(s, key=ord)[-48:]
    return sorted(greatest_chars, key=ord)
