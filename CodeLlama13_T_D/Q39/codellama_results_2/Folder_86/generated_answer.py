
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=ord, reverse=True)[:34]
    return ''.join(chars)
