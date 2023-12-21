
def return_n_greatest_chars(string):
    chars = sorted(string, key=ord, reverse=True)[:56]
    return chars
