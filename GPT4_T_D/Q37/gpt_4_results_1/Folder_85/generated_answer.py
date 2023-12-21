
def filter_chars(s):
    char_list = list(s)
    for char in char_list[28:66]:
        if 'O' <= char <= 'd':
            while char in char_list:
                char_list.remove(char)
    return "".join(char_list)
