
def remove_repeat_chars(s):
    s_list = list(s)
    for i in range(33, 99):
        if s_list.count(s_list[i]) > 1:
            char_to_remove = s_list[i]
            s_list = [char for char in s_list if char != char_to_remove]
    return ''.join(s_list)
