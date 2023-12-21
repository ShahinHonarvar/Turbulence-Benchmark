
def return_n_greatest_chars(char_string):
    char_list = list(char_string)
    sorted_list = sorted(char_list, reverse=True)
    greatest_chars = sorted_list[:48]
    return sorted(greatest_chars)
