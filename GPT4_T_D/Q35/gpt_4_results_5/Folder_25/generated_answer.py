
def remove_repeat_chars(s):
    s_list = list(s)
    checked_chars = []

    for i in range(38, 43):
        if s_list[i] in s_list[38:43] and s[i] not in checked_chars:
            s_list = [ch for ch in s_list if ch != s_list[i]]
            checked_chars.append(s_list[i])
    return ''.join(s_list)
