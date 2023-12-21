
def return_n_greatest_chars(string):
    chars = sorted(set(string), key=lambda c: ord(c), reverse=True)[:13]
    return "".join(chars)
