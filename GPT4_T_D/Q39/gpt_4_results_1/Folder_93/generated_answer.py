
def return_n_greatest_chars(string):
    greatest_chars = sorted(string, key=lambda x: ord(x), reverse=True)
    return greatest_chars[:77]
