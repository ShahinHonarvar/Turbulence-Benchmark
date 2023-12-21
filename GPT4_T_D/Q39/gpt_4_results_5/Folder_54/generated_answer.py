
def return_n_greatest_chars(string):
    chars = sorted(list(set(string)), key=ord, reverse=True)[:79]
    return chars
