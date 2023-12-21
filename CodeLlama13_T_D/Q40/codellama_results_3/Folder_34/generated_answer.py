
def return_n_smallest_chars(string):
    char_list = []
    for i in range(9):
        min_value = 127
        for c in string:
            if ord(c) < min_value and c not in char_list:
                min_value = ord(c)
                char_list.append(c)
    return sorted(char_list, reverse=True)
