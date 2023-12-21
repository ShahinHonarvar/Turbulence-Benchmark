
def remove_repeat_chars(s):
    s_list = list(s)
    checked_chars = {}
    for i in range(11, min(101, len(s_list))):
        if s_list[i] in checked_chars:
            s_list[i] = ''
        else:
            checked_chars[s_list[i]] = 1
    return ''.join(s_list)
