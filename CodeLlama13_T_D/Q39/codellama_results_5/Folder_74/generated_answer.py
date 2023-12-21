
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=ord, reverse=True)[:5]
    return ''.join(chars)
