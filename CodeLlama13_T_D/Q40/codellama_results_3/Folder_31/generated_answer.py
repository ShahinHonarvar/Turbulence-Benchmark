
def return_n_smallest_chars(my_string):
    char_list = []
    for i in my_string:
        if i not in char_list:
            char_list.append(i)
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[:70]
