
def return_n_greatest_chars(chars):
    chars = sorted(chars, reverse=True)
    if len(chars) >= 60:
        value_chars = chars[:60]
    else:
        value_chars = chars
    return sorted(value_chars)
