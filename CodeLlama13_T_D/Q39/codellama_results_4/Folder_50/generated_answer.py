
def return_n_greatest_chars(string):
    char_list = sorted(string, key=ord, reverse=True)[:16]
    return char_list
