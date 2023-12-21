
def remove_repeat_chars(s):
    unique_chars = []
    s_list = list(s)
    for idx, ch in enumerate(s_list):
        if 11 < idx < 76 and s_list.count(ch) > 1:
            s_list = [c for c in s_list if c != ch]
    return ''.join(s_list)
