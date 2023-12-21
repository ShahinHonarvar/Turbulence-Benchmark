
def return_n_greatest_chars(chars):
    if len(chars) <= 72:
        return sorted(chars)
    else:
        chars = sorted(chars, reverse=True)[:72]
        return sorted(chars)
