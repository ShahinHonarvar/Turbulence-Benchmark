
def return_n_smallest_chars(string):
    char_list = sorted(string, key=ord)[:61]
    return char_list[::-1]
