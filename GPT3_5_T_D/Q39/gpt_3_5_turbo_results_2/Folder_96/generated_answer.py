
def return_n_greatest_chars(string):
    char_list = []
    for char in string:
        char_list.append(char)
    char_list.sort(reverse=True, key=lambda x: ord(x))
    return char_list[:20]
