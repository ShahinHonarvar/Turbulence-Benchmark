
def return_n_greatest_chars(s):
    ascii_s = sorted(s, key=ord, reverse=True)
    return ascii_s[:29]
