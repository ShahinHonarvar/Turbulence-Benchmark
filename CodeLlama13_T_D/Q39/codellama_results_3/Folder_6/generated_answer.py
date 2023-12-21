
def return_n_greatest_chars(string):
    char_list = list()
    for i in range(47):
        char_list.append(sorted(string, key=ord, reverse=True)[i])
    return char_list
