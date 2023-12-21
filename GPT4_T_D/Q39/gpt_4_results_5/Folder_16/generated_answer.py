
def return_n_greatest_chars(char_string):
    sorted_chars_list = sorted(char_string, key=ord, reverse=True)
    return sorted_chars_list[:64]
