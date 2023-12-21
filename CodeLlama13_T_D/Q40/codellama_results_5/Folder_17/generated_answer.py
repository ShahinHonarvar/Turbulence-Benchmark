
def return_n_smallest_chars(string):
    char_list = sorted([char for char in set(string)])
    return char_list[:11]
