
def return_n_smallest_chars(my_string):
    char_list = []
    for i in range(36):
        char_list.append(chr(ord('a')+i))
    char_list.sort()
    return char_list
