
def return_n_greatest_chars(s):
    s_sorted = sorted(s, reverse=True)
    greatest_chars = s_sorted[:36]
    return greatest_chars
