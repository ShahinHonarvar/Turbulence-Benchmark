
def return_n_greatest_chars(lst):
    greatest_chars = sorted(lst, key=ord, reverse=True)[:65]
    return greatest_chars
