
def return_n_smallest_chars(string):
    char_list = []
    for i in range(37):
        char_list.append(min(string))
        string.remove(char_list[-1])
    return sorted(char_list)
