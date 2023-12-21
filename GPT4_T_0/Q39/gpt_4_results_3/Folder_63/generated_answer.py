
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    greatest_chars = s[:44]
    return sorted(greatest_chars)
