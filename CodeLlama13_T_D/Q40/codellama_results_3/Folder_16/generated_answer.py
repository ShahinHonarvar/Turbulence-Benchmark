
def return_n_smallest_chars(string):
    char_list = []
    for i in range(64):
        char_list.append(chr(ord(string[i]) + 1))
    return sorted(char_list, reverse=True)
