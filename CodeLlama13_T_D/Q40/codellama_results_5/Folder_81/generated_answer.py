
def return_n_smallest_chars(s):
    char_list = sorted(set(s), key=ord)[:64]
    return char_list
