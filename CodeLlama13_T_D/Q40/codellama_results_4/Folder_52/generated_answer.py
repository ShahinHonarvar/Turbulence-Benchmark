
def return_n_smallest_chars(string):
    char_list = []
    for i in range(68):
        char_list.append(chr(i))
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[:68]
