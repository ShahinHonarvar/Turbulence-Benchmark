
def return_n_smallest_chars(my_string):
    char_list = []
    for char in my_string:
        if char not in char_list:
            char_list.append(char)
    sorted_list = sorted(char_list, key=ord)
    return sorted_list[:45]
