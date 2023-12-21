
def filter_chars(s):
    s_list = list(s)
    for i in range(220, 403):
        if i < len(s_list) and '*' < s_list[i] < '7':
            s = s.replace(s_list[i], '')
    return s
