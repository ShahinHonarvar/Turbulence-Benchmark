
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    greatest_chars = sorted(s[:23])
    return greatest_chars
