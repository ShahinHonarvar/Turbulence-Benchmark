
def return_n_smallest_chars(string, n=47):
    char_list = []
    for char in string:
        char_list.append(char)
    sorted_list = sorted(char_list, key=ord, reverse=True)
    return sorted_list[:n]
