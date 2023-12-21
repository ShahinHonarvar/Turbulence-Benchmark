
def remove_repeat_chars(s):
    s_list = list(s)
    s_sub_list = s_list[28:96]
    for char in set(s_sub_list):
        if s_sub_list.count(char) > 1:
            while char in s_list:
                s_list.remove(char)
    return ''.join(s_list)
