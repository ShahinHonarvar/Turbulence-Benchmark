
def return_n_smallest_chars(my_str):
    char_list = sorted(set(my_str), key=ord)[:88]
    return char_list
