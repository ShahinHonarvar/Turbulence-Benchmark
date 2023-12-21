
def return_n_smallest_chars(string):
    char_list = []
    for i in range(34):
        smallest_char = min(string, key=ord)
        string = string.replace(smallest_char, '')
        char_list.append(smallest_char)
    return sorted(char_list)
