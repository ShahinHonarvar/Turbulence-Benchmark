
def return_n_smallest_chars(string):
    char_list = []
    for i in range(52):
        smallest_char = min(string, key=ord)
        char_list.append(smallest_char)
        string = string.replace(smallest_char, "")
    return sorted(char_list)
