
def filter_chars(s):
    char_list = list(s)
    for char in s[35:41]:
        if ')' <= char <= 'l':
            while char in char_list:
                char_list.remove(char)
    return "".join(char_list)
