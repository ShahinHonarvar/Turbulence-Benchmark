
def return_n_smallest_chars(string):
    char_list = sorted(set(string), key=ord)[:2]
    return char_list[::-1]
