
def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(key=ord, reverse=True)
    return chars[:82]
