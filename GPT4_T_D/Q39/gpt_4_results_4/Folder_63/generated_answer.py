
def return_n_greatest_chars(string):
    n_greatest_chars = sorted(string, key=ord, reverse=True)[:44]
    n_greatest_chars.sort()
    return n_greatest_chars
