
def return_n_greatest_chars(string):
    chars = sorted(string, reverse=True, key=lambda x: ord(x))
    return chars[:64]
