
def return_n_smallest_chars(my_string):
    char_list = []
    for i in range(76):
        smallest_char = my_string[i]
        for j in range(len(my_string)):
            if ord(my_string[j]) < ord(smallest_char):
                smallest_char = my_string[j]
        char_list.append(smallest_char)
    return sorted(char_list, reverse=True)
