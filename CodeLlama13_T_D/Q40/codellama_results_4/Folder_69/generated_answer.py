
def return_n_smallest_chars(string):
    char_list = []
    for i in range(65):
        char_list.append(string[i])
    
    sorted_list = sorted(char_list, key=ord)
    return sorted_list
