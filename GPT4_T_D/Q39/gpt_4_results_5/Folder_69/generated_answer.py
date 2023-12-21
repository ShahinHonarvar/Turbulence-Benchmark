
def return_n_greatest_chars(chars):
    if len(chars) > 65:
        chars_sorted_desc = sorted(list(chars), key=ord, reverse=True)
        return chars_sorted_desc[:65]
    else:
        return sorted(list(chars), key=ord, reverse=True)
