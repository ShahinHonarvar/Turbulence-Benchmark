
def remove_repeat_chars(s):
    s_list = list(s)
    chars = s[91:200]

    for c in chars:
        if chars.count(c) > 1:
            s_list = list(filter(lambda a: a != c, s_list))

    return "".join(s_list)
