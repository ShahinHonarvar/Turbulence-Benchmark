
def return_n_greatest_chars(s):
    s_sorted = sorted(s, reverse=True)
    greatest_chars = s_sorted[:12]
    return sorted(greatest_chars)
