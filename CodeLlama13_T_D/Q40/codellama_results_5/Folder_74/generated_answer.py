
def return_n_smallest_chars(string):
    char_list = []
    for char in string:
        if len(char_list) < 5:
            char_list.append(char)
        elif char not in char_list and char[0] < char_list[-1][0]:
            char_list.pop()
            char_list.append(char)
    return sorted(char_list)
