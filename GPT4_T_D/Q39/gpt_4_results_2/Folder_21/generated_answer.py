
def return_n_greatest_chars(s):
    s_sorted = sorted(s, key=ord, reverse=True)
    return s_sorted[:44]
