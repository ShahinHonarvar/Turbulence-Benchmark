
def return_n_smallest_chars(string):

    small_chars_list = sorted(list(string), key=ord)[:64]
    return small_chars_list
