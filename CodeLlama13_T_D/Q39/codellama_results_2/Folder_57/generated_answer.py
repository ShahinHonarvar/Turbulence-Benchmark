
def return_n_greatest_chars(string):
    chars = sorted(string, key=lambda x: ord(x), reverse=True)[:29]
    return "".join(chars)
