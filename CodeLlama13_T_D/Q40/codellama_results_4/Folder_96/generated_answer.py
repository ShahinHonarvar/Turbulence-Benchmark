
def return_n_smallest_chars(string):
    char_list = sorted([char for char in string if char != ''])
    return char_list[:20]
