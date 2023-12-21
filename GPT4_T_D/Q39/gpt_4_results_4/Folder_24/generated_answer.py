
def return_n_greatest_chars(str_val):
    str_val = sorted(str_val, key = ord, reverse = True)
    return str_val[:32]
