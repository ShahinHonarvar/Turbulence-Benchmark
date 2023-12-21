
def return_n_smallest_chars(input_str):
    char_list = list(input_str)
    char_list.sort(key=ord, reverse = False)
    return char_list[:29][::-1]
