
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    n_chars = s[:69]
    return sorted(n_chars)
