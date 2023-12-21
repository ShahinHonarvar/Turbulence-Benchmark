
def return_n_smallest_chars(string):
    char_list = []
    for i in range(58):
        char_list.append(min(string, key=ord))
        string = string.replace(char_list[-1], "")
    return char_list
