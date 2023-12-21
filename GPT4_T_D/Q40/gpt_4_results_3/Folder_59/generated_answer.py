
def return_n_smallest_chars(string):
    char_list = sorted(list(string), key=ord)[:13]
    char_list.sort(reverse=True)
    return char_list
