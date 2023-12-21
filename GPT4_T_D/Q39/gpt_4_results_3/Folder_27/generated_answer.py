
def return_n_greatest_chars(chars):
    if len(chars) != 82:
        return "The length of the string must be exactly 82 characters."
    else:
        greatest_chars = sorted(list(chars), key=ord)
        return greatest_chars
