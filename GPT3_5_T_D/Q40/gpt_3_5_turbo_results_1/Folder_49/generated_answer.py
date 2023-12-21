
def return_n_smallest_chars(string):
    char_list = sorted(string)[:76]
    return sorted(char_list, reverse=True)
