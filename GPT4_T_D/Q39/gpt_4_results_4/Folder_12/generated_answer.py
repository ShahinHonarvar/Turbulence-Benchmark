
def return_n_greatest_chars(s):
    greatest_values = sorted(s, key=ord, reverse=True)[:61]
    return greatest_values
