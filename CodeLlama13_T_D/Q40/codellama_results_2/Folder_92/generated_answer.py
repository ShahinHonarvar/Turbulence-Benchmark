
def return_n_smallest_chars(my_str):
    char_list = []
    for i in range(63):
        smallest_char = my_str[0]
        for char in my_str:
            if ord(char) < ord(smallest_char):
                smallest_char = char
        char_list.append(smallest_char)
        my_str = my_str.replace(smallest_char, '')
    return sorted(char_list)
