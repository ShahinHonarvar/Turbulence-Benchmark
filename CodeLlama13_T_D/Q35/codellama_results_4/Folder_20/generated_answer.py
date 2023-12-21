
def remove_repeat_chars(s):
    s_list = list(s)
    for i in range(27, 96):
        if s_list[i] in s_list:
            s_list.remove(s_list[i])
    return ''.join(s_list)
