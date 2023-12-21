
def remove_repeat_chars(s):
    s_list = list(s)
    check_chars = s[87:90]
    for char in check_chars:
        if check_chars.count(char) > 1:
            while char in s_list:
                s_list.remove(char)
    return ''.join(s_list)
