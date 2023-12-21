
def return_n_greatest_chars(string):
    chars = sorted(list(set(string)), key=lambda x: ord(x), reverse=True)[:31]
    return chars
