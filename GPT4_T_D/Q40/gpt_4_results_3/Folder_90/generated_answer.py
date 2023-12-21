
def return_n_smallest_chars(char_string):
    char_list = sorted(list(set(char_string)), key=ord)
    char_list_24 = char_list[:24]
    char_list_24.sort(reverse=True)
    return char_list_24
