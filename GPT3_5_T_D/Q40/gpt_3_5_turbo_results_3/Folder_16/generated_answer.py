
def return_n_smallest_chars(string):
    char_list = list(string)
    sorted_list = sorted(char_list)
    smallest_chars = sorted_list[:64]
    return sorted(smallest_chars, reverse=True)
