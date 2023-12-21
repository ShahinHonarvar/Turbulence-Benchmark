
def return_n_greatest_chars(char_string):
    char_string = sorted(char_string, reverse=True)[:49]
    return char_string
