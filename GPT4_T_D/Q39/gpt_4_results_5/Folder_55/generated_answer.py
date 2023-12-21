
def return_n_greatest_chars(chars):
    chars_list = list(chars)
    chars_list.sort(key=ord, reverse=True)
    return chars_list[:75]
