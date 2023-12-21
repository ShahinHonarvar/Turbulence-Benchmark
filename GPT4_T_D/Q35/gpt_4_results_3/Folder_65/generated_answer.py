
def remove_repeat_chars(s):
    s_list = list(s)
    char_dict = {}
    for i in range(52, 76):
        if i < len(s_list):
            if s_list[i] in char_dict:
                char_dict[s_list[i]] += 1
            else:
                char_dict[s_list[i]] = 1

    to_remove = [char for char, count in char_dict.items() if count > 1]

    return ''.join([char for char in s_list if char not in to_remove])
