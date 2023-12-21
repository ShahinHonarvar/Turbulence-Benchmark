
def return_n_greatest_chars(my_string):
    char_list = sorted([char for char in my_string], key=ord, reverse=True)[:46]
    return ''.join(char_list)
