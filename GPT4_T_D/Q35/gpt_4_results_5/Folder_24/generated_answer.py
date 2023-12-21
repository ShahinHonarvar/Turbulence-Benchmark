
def remove_repeat_chars(s):
    s_list = list(s)
    char_count = {}
    for i in range(len(s_list)):
        if 13 < i < 91:
            if s_list[i] in char_count:
                char_count[s_list[i]] += 1
            else:
                char_count[s_list[i]] = 1
    for char, count in char_count.items():
        if count > 1:
            while char in s_list:
                s_list.remove(char)
    return "".join(s_list)
