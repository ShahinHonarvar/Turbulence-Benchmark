
def return_n_smallest_chars(char_string):
    ascii_list = [char for char in char_string]
    ascii_list.sort(key=ord)
    return ascii_list[:35]
