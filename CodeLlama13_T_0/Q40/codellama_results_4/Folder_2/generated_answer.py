
def return_n_smallest_chars(string):
    char_list = []
    for i in range(48):
        char_list.append(min(string))
        string = string.replace(min(string), "")
    return char_list
