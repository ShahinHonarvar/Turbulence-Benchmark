
def return_n_greatest_chars(string):
    char_list = sorted([char for char in string], key=ord)
    return char_list[-10:]
