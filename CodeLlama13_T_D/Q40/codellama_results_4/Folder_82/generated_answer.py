
def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)))
    return char_list[:60]
