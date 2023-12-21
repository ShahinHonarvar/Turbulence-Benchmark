
def filter_chars(s):
    s_list = list(s)
    for char in s_list[32:50]:
        if '/' < char < 'J':
            s = s.replace(char, '')
    return s
