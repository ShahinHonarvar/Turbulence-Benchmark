
def return_n_smallest_chars(string):
    char_list = []
    for c in string:
        if c not in char_list:
            char_list.append(c)
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[:82]
