
def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    char_list.sort()
    return char_list[0:39]
