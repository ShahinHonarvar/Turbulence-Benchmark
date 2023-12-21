
def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=ord, reverse=True)
    return chars[:3]
