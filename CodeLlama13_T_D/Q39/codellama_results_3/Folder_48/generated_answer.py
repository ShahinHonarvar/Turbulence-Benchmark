
def return_n_greatest_chars(my_string):
    char_list = list(set(my_string))
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:12]
    return sorted_char_list
