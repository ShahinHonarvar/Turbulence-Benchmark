
def return_n_greatest_chars(chars):
    sorted_string = sorted(chars, reverse=True)
    greatest_chars = sorted_string[:3]
    return sorted(greatest_chars)
