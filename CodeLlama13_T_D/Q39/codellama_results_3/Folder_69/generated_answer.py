
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=ord, reverse=True)[:65]
    return ''.join(chars)
