
def return_n_smallest_chars(string):
    char_list = sorted(list(string), key=ord)[:58]
    return char_list
