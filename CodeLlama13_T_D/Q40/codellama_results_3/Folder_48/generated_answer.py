
def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    
    sorted_char_list = sorted(char_list, key=ord)
    
    return sorted_char_list[:12]
