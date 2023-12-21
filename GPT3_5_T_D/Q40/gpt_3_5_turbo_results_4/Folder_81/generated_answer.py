
def return_n_smallest_chars(s):
    char_list = list(s)
    char_list.sort()
    return char_list[:64]
