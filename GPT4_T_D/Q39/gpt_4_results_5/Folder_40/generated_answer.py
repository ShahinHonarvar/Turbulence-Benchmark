
def return_n_greatest_chars(char_str):
    char_list = sorted(list(char_str), reverse=True)[:7]
    return char_list
