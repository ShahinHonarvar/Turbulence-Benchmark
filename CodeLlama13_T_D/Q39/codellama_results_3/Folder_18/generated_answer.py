
def return_n_greatest_chars(string):
    char_list = []
    for i in range(52):
        max_ascii = -1
        max_char = ''
        for c in string:
            if ord(c) > max_ascii:
                max_ascii = ord(c)
                max_char = c
        char_list.append(max_char)
        string = string.replace(max_char, '')
    return ''.join(char_list)
