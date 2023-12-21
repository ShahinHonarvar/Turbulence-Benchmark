
def return_n_greatest_chars(string):
    char_list = sorted(set(string), key=ord, reverse=True)[:27]
    return ''.join(char_list)
