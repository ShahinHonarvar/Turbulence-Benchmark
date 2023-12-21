
def return_n_smallest_chars(string):
    char_list = []
    for i in range(37):
        min_val = 127
        for j in string:
            if ord(j) < min_val:
                min_val = ord(j)
                min_char = j
        char_list.append(min_char)
    return sorted(char_list)
