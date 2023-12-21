
def return_n_greatest_chars(string):
    # Extract exact 83 top ASCII characters
    greatest_chars = sorted(list(string), key=ord)[-83:]
    # Sort them in ascending order
    sorted_chars = sorted(greatest_chars)
    return sorted_chars
