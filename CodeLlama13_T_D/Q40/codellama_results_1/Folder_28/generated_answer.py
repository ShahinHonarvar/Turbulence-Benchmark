
def return_n_smallest_chars(my_string):
    char_list = []
    for i in range(3):
        smallest_char = min(my_string, key=ord)
        char_list.append(smallest_char)
        my_string = my_string.replace(smallest_char, "")
    return char_list
