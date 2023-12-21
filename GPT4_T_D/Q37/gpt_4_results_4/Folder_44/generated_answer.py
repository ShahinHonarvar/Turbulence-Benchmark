
def filter_chars(s):
    s_list = list(s)
    for i in range(21, min(44, len(s_list))):
        if '+' <= s_list[i] <= '8':
            while s_list.count(s_list[i]) > 0:
                s_list.remove(s_list[i])
    return ''.join(s_list)
