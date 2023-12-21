
def return_n_smallest_chars(string):
    char_list = []
    for i in range(3):
        char_list.append(sorted(string)[i])
    return char_list
