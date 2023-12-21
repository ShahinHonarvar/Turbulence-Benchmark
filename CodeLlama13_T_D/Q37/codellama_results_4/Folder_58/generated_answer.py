
def filter_chars(s):
    s_list = list(s)
    for i in range(503, 754):
        if '9' <= s_list[i] <= 'w':
            s_list.remove(s_list[i])
    return "".join(s_list)
