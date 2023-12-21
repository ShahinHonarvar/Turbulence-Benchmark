
def return_n_smallest_chars(string):
    char_list = sorted(string, key=ord)
    return char_list[:47]
