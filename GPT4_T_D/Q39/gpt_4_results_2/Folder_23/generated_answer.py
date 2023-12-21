
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    n_greatest_chars = sorted(s[0:46])
    return n_greatest_chars
