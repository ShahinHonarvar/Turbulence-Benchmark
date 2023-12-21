
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)
    greatest_ascii_chars = sorted_chars[:29]
    return sorted(greatest_ascii_chars)
