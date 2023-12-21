
def return_n_smallest_chars(string):
    char_list = sorted(set(string))
    return sorted(char_list, key=ord)[:57]
