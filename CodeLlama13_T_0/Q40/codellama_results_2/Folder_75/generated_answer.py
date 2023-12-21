
def return_n_smallest_chars(string):
    char_list = sorted(set(string))
    return char_list[:2]
