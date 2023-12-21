
def return_n_smallest_chars(string):
    char_list = sorted(list(set(string)), key=ord)[:46]
    return char_list
