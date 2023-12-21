
def return_n_greatest_chars(char_string):
    char_list = sorted(char_string, reverse=True)
    result = sorted(char_list[:17])
    return result
