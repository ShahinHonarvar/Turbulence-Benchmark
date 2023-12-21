
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    greatest_ascii = sorted_chars[:68]
    return greatest_ascii
