
def return_n_greatest_chars(string):
    chars = list(string)
    chars.sort(reverse=True)
    return chars[:66]
