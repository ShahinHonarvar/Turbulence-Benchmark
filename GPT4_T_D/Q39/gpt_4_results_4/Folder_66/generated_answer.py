
def return_n_greatest_chars(s):
    greatest_chars = sorted(s, key=ord, reverse=True)[:33]
    return greatest_chars
