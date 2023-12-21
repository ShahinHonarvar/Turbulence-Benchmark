
def return_n_smallest_chars(str_chars):
    if len(set(str_chars)) < 8:
        return "The string does not have enough distinct characters."
    else:
        char_list = list(set(str_chars))
        char_list.sort(key=ord)
        return char_list[:8]
