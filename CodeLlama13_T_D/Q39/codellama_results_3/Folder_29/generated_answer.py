
def return_n_greatest_chars(string):
    char_list = list()
    for c in string:
        if c not in char_list:
            char_list.append(c)
    sorted_char_list = sorted(char_list, key=lambda x: ord(x), reverse=True)[:23]
    return ''.join(sorted_char_list)
