
def return_n_smallest_chars(char_string):
    char_list = sorted([char for char in char_string])
    if len(char_list) > 73:
        char_list = char_list[:73]
    return char_list
