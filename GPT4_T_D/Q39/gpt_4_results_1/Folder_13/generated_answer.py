
def return_n_greatest_chars(s):
    sorted_string = sorted(s, reverse=True)
    greatest_chars = sorted_string[:31]
    return sorted(greatest_chars)
