
def return_n_greatest_chars(string):
    chars = sorted(string, reverse=True)[:38]
    return sorted(chars)
