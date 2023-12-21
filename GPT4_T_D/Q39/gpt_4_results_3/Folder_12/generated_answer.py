
def return_n_greatest_chars(s):
    return sorted(list(s), key=ord, reverse=True)[:61]
