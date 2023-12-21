
def filter_chars(s):
    char_list = list(s)
    for char in char_list[62:88]:
        if '%' < char < 'q':
            s = s.replace(char, '')
    return s
