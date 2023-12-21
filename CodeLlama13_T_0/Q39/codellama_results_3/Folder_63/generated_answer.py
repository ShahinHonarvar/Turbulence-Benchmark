
def return_n_greatest_chars(string):
    char_list = sorted(set(string), key=ord)
    return char_list[-44:]
