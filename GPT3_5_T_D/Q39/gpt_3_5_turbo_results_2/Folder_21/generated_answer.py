
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, reverse=True)
    greatest_chars = sorted_chars[:44]
    return greatest_chars
