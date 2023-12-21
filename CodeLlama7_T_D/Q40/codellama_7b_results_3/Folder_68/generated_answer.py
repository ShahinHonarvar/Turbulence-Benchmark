
def return_n_smallest_chars(string, n=89):
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.sort(key=ord, reverse=True)
    return char_list[:n]
