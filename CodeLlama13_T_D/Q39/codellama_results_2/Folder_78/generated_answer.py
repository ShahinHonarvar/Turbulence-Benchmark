
def return_n_greatest_chars(my_string):
    char_list = sorted(my_string, key=ord, reverse=True)[:43]
    return char_list
