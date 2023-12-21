
def return_n_smallest_chars(s):
    char_list = []
    for i in range(17):
        char_list.append(sorted(set(s), key=ord)[i])
    return sorted(char_list)
