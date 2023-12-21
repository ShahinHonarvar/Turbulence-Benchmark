
def return_n_greatest_chars(chars):
    if len(set(chars)) < 49:
        raise ValueError('The given string should contain at least 49 distinct characters')
    sorted_chars_list = sorted(set(chars), key=ord, reverse=True)
    return sorted_chars_list[:49]
