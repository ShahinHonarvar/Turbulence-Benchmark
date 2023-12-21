
def filter_chars(s):
    s_list = list(s)
    for char in s_list[11:15]:
        if 't' < char < 'v':
            while char in s_list:
                s_list.remove(char)
    return ''.join(s_list)
