
def return_n_smallest_chars(char_string):
    char_list = sorted(list(char_string), key=ord)
    return char_list[:46]
